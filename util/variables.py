import argparse

# We give the line a minimum length, to make it more visible
min_line_length = 50

parser = argparse.ArgumentParser(
    description="Create artwork based on 'De Stijl' style "
    "but every angle is slightly off and all the "
    "colours are not the primary colours"
)
parser.add_argument(
    "--seed",
    default="The Stijl",
    help="The seed string of the artwork (default 'The Stijl')",
)
parser.add_argument(
    "--width", default=800, help="The width of the canvas as integer (default: 800)"
)
parser.add_argument(
    "--height", default=600, help="The width of the canvas as integer (default: 600)"
)
parser.add_argument(
    "--min_squares",
    default=0,
    help="It will draw a random amount of squares based on "
    "the seed between `min_squares` and `max_squares`. "
    "The `min_squares` is the integer variable to determine the minimal amount of squares (default: 0)",
)
parser.add_argument(
    "--max_squares",
    default=20,
    help="It will draw a random amount of squares based on "
    "the seed between `min_squares` and `max_squares`. "
    "The `max_squares` is the integer variable to determine the maximum amount of squares (default: 20)",
)
parser.add_argument(
    "--view_algorithm",
    default=True,
    help="If True the canvas will expand and you can see the "
    "algorithm perform it's steps. "
    "If set to False the algorithm will finish "
    "as quick as possible and store images of the final canvas",
)
parser.add_argument(
    "--angles",
    default=[88, 89, 91, 92],
    help="Indicate what angles can be created. Here you can specify how crooked or how straight the created planes should be by specifying the possible corner angles. (default: 88,89,91,91)",
)
parser.add_argument(
    "--show_lines",
    default=True,
    help="If True the image will have black outlines around the area's.",
)
args = parser.parse_args()

width = int(args.width)
height = int(args.height)
min_squares = int(args.min_squares)
max_squares = int(args.max_squares)

# angles = [88, 89, 91, 92]
#
# seed = "The Stijl"

angles = args.angles
if isinstance(angles, str):
    angles = list(map(int, angles.split(",")))
seed = args.seed

view_algorithm = True
if args.view_algorithm == "False":
    view_algorithm = False

show_lines = True
if args.show_lines == "False":
    show_lines = False

turtle_speed = 5
if not view_algorithm:
    turtle_speed = 0

print(args)
