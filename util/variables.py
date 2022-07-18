import argparse

# We give the line a minimum length, to make it easier with painting and visibly
min_line_length = 50

angles = [88, 89, 91, 92]

seed = "The Stijl"

parser = argparse.ArgumentParser(
    description="Create artwork based on 'De Stijl' style but every angle is slightly off and all the colours are not the primary colours"
)
parser.add_argument(
    "--seed", default="The Stijl", help="The seed of the artwork (default 'The Stijl')"
)
parser.add_argument(
    "--width", default=800, help="The width of the canvas (default: 800)"
)
parser.add_argument(
    "--height", default=600, help="The width of the canvas (default: 600)"
)
parser.add_argument(
    "--min_squares",
    default=0,
    help="It will draw a random amount of squares based on the seed between `min_squares` and `max_squares`. The `min_squares` is the minimal amount of squares (default:0)",
)
parser.add_argument(
    "--max_squares",
    default=20,
    help="It will draw a random amount of squares based on the seed between `min_squares` and `max_squares`. The `max_squares` is the maximum amount of squares (default:20)",
)
parser.add_argument(
    "--view_algorithm",
    default=True,
    help="If True the canvas will expand and you can see the algorithm perform it's steps. If set to False the algorithm will finish as quick as possible and store images of the final canvas",
)
args = parser.parse_args()

width = args.width
height = args.height
min_squares = args.min_squares
max_squares = args.max_squares

view_algorithm = True
if args.view_algorithm == "False":
    view_algorithm = False

turtle_speed = 5
if not view_algorithm:
    turtle_speed = 0

print(args)
