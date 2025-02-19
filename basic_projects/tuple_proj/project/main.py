from config import get_user_input, configure_environment
from data_processing import create_tuple1, create_tuple2, create_tuple3, create_tuple4, create_tuple5
from utils import sink1, sink2, sink3, sink4, sink5


def main():
    # Configure the environment
    configure_environment()

    # Get tainted variable from user input
    taint_var = get_user_input()

    # Create tuples and process data
    tuple1 = create_tuple1(taint_var)
    tuple2 = create_tuple2(taint_var)
    tuple3 = create_tuple3(taint_var)
    tuple4 = create_tuple4(taint_var)
    tuple5 = create_tuple5(taint_var)

    # Pass the data to the sink
    sink1(tuple1)
    sink2(tuple2)
    sink3(tuple3)
    sink4(tuple4)
    sink5(tuple5)


if __name__ == "__main__":
    main()