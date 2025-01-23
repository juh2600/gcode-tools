#!/usr/bin/fish

# This script uses the name it was invoked as to represent the instruction in
# the block. Run something like:
#   $ for n in (seq 0 99) 0(seq 0 9) 54.1 154 (seq 110 129) 90.1 91.1 92.(seq 1 3); ln -s G.fish G$n; end
#   $ for c in M(seq 0 99) F S T X Y Z A; ln -s G.fish $c; end
# and so on for whatever instructions you need that i have forgorren
# then invoke as:
#   $ G00 X0 Y10 # send this block
#   $ G01 -h # for help
# i'm sorry i'm tired you're on your own after that. but the script args are
# listed out at `argparse' below, and you can set env vars DEFAULT_TARGET and
# DEFAULT_BAUD or specify on the command line. if you don't have picocom, fix
# it up in the last line.

if [ -z "$DEFAULT_TARGET" ]
	set DEFAULT_TARGET /dev/ttyUSB0
end
if [ -z "$DEFAULT_BAUD" ]
	set DEFAULT_BAUD 115200
end

if not which color >/dev/null
	function color
	end
end

argparse 't/target=' 'b/baud=' 'd/debug' 'h/help' -- $argv
if status basename | grep -Eq 'fish'
	set code $argv[1]
	set --erase argv[1]
else
	set code (status basename)
	if [ "$code" = "x" ]
		set code X
	end
	switch $code
		case X Y Z F S T A
			echo >/dev/stderr '(WW)' Invoking $code directly is not yet supported! Prefix with a G code if the command does not behave as expected.
			set code $code$argv[1]
			set --erase argv[1]
	end
end

if set -q _flag_help
	# List command parameters
	switch $code
		case G0 G00
			set params '[X] [Y] [Z]'
		case G1 G01
			set params '[X] [Y] [Z] [F]'
		case G2 G02 G3 G03
			set params '[X] [Y] [Z] [I] [J] [K] [R] [F]'
		case G4 G04
			set params 'P|X|U|S'
		case G28
			set params '[X] [Y] [Z] [A] [B] [C] [U] [V] [W] [L] [O] [R]'
		case G54.1 G154
			set params 'P'
		case G92
			set params '[X] [Y] [Z] [A] [B] [C] [U] [V] [W] [E]'
		case M104 M140 M190
			set params 'S'
		case M109
			set params 'S|R'
		case M149
			set params 'C|F|K'
		case G(seq 15 19) G(seq 54 59) G(seq 110 129)
			set params ''
		case '*'
			set params 'UNKNOWN PARAMETERS'
	end
	# Brief description
	switch $code
		case G0 G00
			set desc Rapid move to '(X, Y, Z)'. No linear interpolation or synchronization is performed.
		case G1 G01
			set desc Interpolated move to '(X, Y, Z)' at feed rate F.
		case G2 G02
			set desc Clockwise arc. See online help for details.
		case G3 G03
			set desc Counterclockwise arc. See online help for details.
		case G4 G04
			set desc Dwell for a period of time. Unit may be second or millisecond depending on implementation. Parameter name also depends on implementation and may be P, X, or U. Some implementations do not require a parameter, in which case the controller waits for the machine to catch up. See online help for details.
		case G15
			set desc Switch to Cartesian coordinates.
		case G16
			set desc Switch to polar coordinates.
		case G17
			set desc Select the XY plane for commands such as G2, G3, G16, G41-44, and more.
		case G18
			set desc Select the XZ plane for commands such as G2, G3, G16, G41-44, and more.
		case G19
			set desc Select the YZ plane for commands such as G2, G3, G16, G41-44, and more.
		case G20
			set desc Switch to inches.
		case G21
			set desc Switch to millimeters.
		case G28
			set desc Home axes. X-Z, A-C, U-W may be passed as flags to indicate which axes to home, or else all axes will be homed. L restores bed leveling state after homing. O skips homing if position is already trusted. R is a distance to raise nozzle before homing. See also M420.
		case G(seq 54 59) G54.1 G(seq 110 129)
			set desc Switch to a numbered offset. G54-G59 are standard. G54.1 is a common extension syntax that takes P as an index. Haas uses G110-G129 for more indices.
		case G90
			set desc Switch to absolute positioning.
		case G91
			set desc Switch to incremental positioning.
		case G92
			set desc Set work offset \(zero axes\). Specify the desired coordinates to assign to the machine\'s current position. See online help for details.
		case M104
			set desc Begin heating hotend to temperature S, non-blocking.
		case M109
			set desc Heat hotend to temperature 'S|R'. If S, block only for heating. If R, block for heating or cooling.
		case M140
			set desc Begin heating bed to temperature S, non-blocking.
		case M149
			set desc Set temperature unit by specifying one of 'C | F | K'.
		case M190
			set desc Heat bed to temperature S, blocking.
		case '*'
			set desc 'No help string is defined for this command.'
	end
	# Link to article
	switch $code
		case G0 G1 G00 G01
			set url 'https://www.cnccookbook.com/g00-g01-cnc-g-code/'
		case G2 G3 G02 G03
			set url 'https://www.cnccookbook.com/cnc-g-code-arc-circle-g02-g03/'
		case G4 G04
			set url 'https://www.cnccookbook.com/g04-gcode-pause-dwell/'
		case G15 G16
			set url 'https://www.cnccookbook.com/cnc-bolt-circle-g15-g16-gcode-polar-coordinates/'
		case G17 G18 G19
			set url 'https://www.cnccookbook.com/g17-g18-and-g19-g-codes-plane-selection/'
		case G20 G21
			set url 'https://www.cnccookbook.com/g21-gcode-g20-cnc-metric-imperial/'
		case G28
			set url 'https://marlinfw.org/docs/gcode/G028.html'
		case G(seq 52 59) G54.1 G92 G(seq 110 129) G154
			set url 'https://www.cnccookbook.com/g54-g92-g52-work-offsets-cnc-g-code/'
		case G90 G91
			set url 'https://www.cnccookbook.com/g91-g90-g-code-cnc-absolute-incremental-programming/'
		case M104
			set url 'https://marlinfw.org/docs/gcode/M104.html'
		case M109
			set url 'https://marlinfw.org/docs/gcode/M109.html'
		case M140
			set url 'https://marlinfw.org/docs/gcode/M140.html'
		case M149
			set url 'https://marlinfw.org/docs/gcode/M149.html'
		case M190
			set url 'https://marlinfw.org/docs/gcode/M190.html'
		case '*'
			set url 'Not defined for this command'
	end

	# TODO do something with vendor/impl info
	switch $code
		case G4 G04
			set MARLIN P millisecond, S second
	end

	# TODO real fancy: if args are passed such as `G0 Z0 --help',
	# fill in those values in the help text: `G0 [X] [Y] Z0'
	# TODO could also highlight red extraneous parameters, such as `G0 F100'

	echo -e (color blue)$code(color 0) (color yellow)$params(color 0)
	echo
	echo -e $desc
	echo -e Online help: (color blue underline)$url(color normal)
	exit 0
end

if [ -z $_flag_target ]
	set target $DEFAULT_TARGET
else
	set target $_flag_target
end

if [ -z $_flag_baud ]
	set baud "-b $DEFAULT_BAUD"
else
	set baud "-b $_flag_baud"
end

if set -q $_flag_debug
	set output /dev/stdout
else
	set output /dev/null
end

echo $code $argv | sudo picocom $target $baud > $output
