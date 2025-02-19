from config import get_user_input, configure_environment
from data_processing import create_set1, create_set2, create_set3, create_set4
from utils import sink1, sink2, sink3, sink4


def main():
    # Configure the environment
    configure_environment()

    # Get tainted variable from user input
    taint_var = get_user_input()

    # Create sets and process data
    set1 = create_set1(taint_var)
    set2 = create_set2(taint_var)
    set3 = create_set3(taint_var)
    set4 = create_set4(taint_var)

    # Pass the data to the sink
    sink1(set1)
    sink2(set2)
    sink3(set3)
    sink4(set4)


if __name__ == "__main__":
    main()