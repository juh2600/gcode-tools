from gcode_pb2 import Block, Command, Letter, Argument, SingleArgument, MutexArgument, ArgType, Vendor
import re

#class B(Block):
#    def v(self, vendor: Vendor):
#        self.vendor.append(vendor)
#        return self

lettermap = {
      "G": Letter.G
    , "M": Letter.M
    , "T": Letter.T
    , "D": Letter.D
}

typemap = {
      "#": ArgType.NUMBER
    , "z": ArgType.INTEGER
    , "q": ArgType.FLOAT
    , "s": ArgType.STRING
    , "f": ArgType.FILE_PATH
    , "F": ArgType.FLAG
}

arg_parser = re.compile('!?(?P<NAME>[A-Z])(?P<TYPE>[#zqsfF]?)(?:: (?P<DOCSTRING>.*))?$')
def parse_args(args: str):
    out = []
    for arg in args.split(','):
        arg = arg.strip()
        if len(arg) == 0:
            break
        A = Argument()
        A.mandatory = arg[0] == '!'
        if '|' in arg:
            a = MutexArgument()
            for sa in parse_args(arg.replace('|', ',')):
                a.choices.append(sa.solo)
            A.mutex.MergeFrom(a)
        else:
            a = SingleArgument()
            parsed = arg_parser.match(arg.strip())
            try: a.name = parsed['NAME']
            except: pass
            if parsed['TYPE'] == '':
                a.type = ArgType.FLOAT
            else:
                try: a.type = typemap[parsed['TYPE']]
                except: pass
            try: a.description = parsed['DOCSTRING']
            except: pass
            A.solo.MergeFrom(a)
        out.append(A)
    return out

block_parser = re.compile('(?P<LETTER>[A-Z])(?P<NUMBER>[0-9.]*) *(?P<ARGS>[^;]*)?(?: *; *(?P<DOCSTRING>[^@]*))?(?: *@(?P<LOCATION>.*))? *$')
def parseSpec(format: str):
    out = Block()
    parsed = block_parser.match(format).groupdict()
    out.cmd.letter = lettermap[parsed['LETTER']]
    out.cmd.number = parsed['NUMBER']
    for arg in parse_args(parsed['ARGS']):
        out.cmd.args.append(arg)
    out.cmd.description = parsed['DOCSTRING']
    try: out.cmd.url = parsed['LOCATION']
    except: pass
    return out

specs = [
      'G0  X, Y, Z; Rapid move to (X, Y, Z) peformed without guarantee of interpolation or synchronization. @https://www.cnccookbook.com/g00-g01-cnc-g-code/'
    , 'G00 X, Y, Z; Rapid move to (X, Y, Z) peformed without guarantee of interpolation or synchronization. @https://www.cnccookbook.com/g00-g01-cnc-g-code/'
    , 'G1  X, Y, Z, F; Interpolated move to (X, Y, Z) at feed rate F. @https://www.cnccookbook.com/g00-g01-cnc-g-code/'
    , 'G01 X, Y, Z, F; Interpolated move to (X, Y, Z) at feed rate F. @https://www.cnccookbook.com/g00-g01-cnc-g-code/'
    , 'G2  X, Y, Z, I, J, K, R, F; Clockwise arc. See online help for details. @https://www.cnccookbook.com/cnc-g-code-arc-circle-g02-g03/'
    , 'G02 X, Y, Z, I, J, K, R, F; Clockwise arc. See online help for details. @https://www.cnccookbook.com/cnc-g-code-arc-circle-g02-g03/'
    , 'G3  X, Y, Z, I, J, K, R, F; Counterclockwise arc. See online help for details. @https://www.cnccookbook.com/cnc-g-code-arc-circle-g02-g03/'
    , 'G03 X, Y, Z, I, J, K, R, F; Counterclockwise arc. See online help for details. @https://www.cnccookbook.com/cnc-g-code-arc-circle-g02-g03/'
    # TODO define G04 more rigorously with vendor details
    , 'G4  P|X|U|S; Dwell for a period of time. Unit and argument name depend on VENDOR. Some implementations do not require an argument, in which case the controller waits for the machine to catch up. See online help for details. @https://www.cnccookbook.com/g04-gcode-pause-dwell/'
    , 'G04 P|X|U|S; Dwell for a period of time. Unit and argument name depend on VENDOR. Some implementations do not require an argument, in which case the controller waits for the machine to catch up. See online help for details. @https://www.cnccookbook.com/g04-gcode-pause-dwell/'
    , 'G15; Switch to Cartesian coordinates. @https://www.cnccookbook.com/cnc-bolt-circle-g15-g16-gcode-polar-coordinates/'
    , 'G16; Switch to polar coordinates. @https://www.cnccookbook.com/cnc-bolt-circle-g15-g16-gcode-polar-coordinates/'
    , 'G17; Select the XY plane for commands such as G2, G3, G16, G41-44, and more. @https://www.cnccookbook.com/g17-g18-and-g19-g-codes-plane-selection/'
    , 'G18; Select the XZ plane for commands such as G2, G3, G16, G41-44, and more. @https://www.cnccookbook.com/g17-g18-and-g19-g-codes-plane-selection/'
    , 'G19; Select the YZ plane for commands such as G2, G3, G16, G41-44, and more. @https://www.cnccookbook.com/g17-g18-and-g19-g-codes-plane-selection/'
    , 'G20; Switch to inches.'
    , 'G21; Switch to millimeters.'
    , 'G28 XF, YF, ZF, AF, BF, CF, UF, VF, WF, LF, OF, Rq; Home axes. X-Z, A-C, U-W may be passed as flags to indicate which axes to home, or else all axes will be homed. L restores bed leveling state after homing. O skips homing if position is already trusted. R is a distance to raise nozzle before homing. See also M420. @https://marlinfw.org/docs/gcode/G028.html'
    # TODO G54-59, G54.1, G110-129
]

entries = [parseSpec(x) for x in specs]