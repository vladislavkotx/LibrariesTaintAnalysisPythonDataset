from config import get_user_input, configure_environment
from data_processing import create_array1, create_array2, create_array3, create_array4
from utils import sink1, sink2, sink3, sink4


def main():
    # Configure the environment
    configure_environment()

    # Get tainted variable from user input
    taint_var = get_user_input()

    # Create arrays and process data
    array1 = create_array1(taint_var)
    array2 = create_array2(taint_var)
    array3 = create_array3(taint_var)
    array4 = create_array4(taint_var)

    # Pass the data to the sink
    sink1(array1)
    sink2(array2)
    sink3(array3)
    sink4(array4)


if __name__ == "__main__":
    main()