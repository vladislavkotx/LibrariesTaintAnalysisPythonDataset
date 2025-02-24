from config import get_user_input, configure_environment
from data_processing import create_dict1, create_dict2, create_dict3
from utils import sink1, sink2, sink3


def main():
    # Configure the environment
    configure_environment()

    # Get tainted variable from user input
    taint_var = get_user_input()

    # Create dicts and process data
    dict1 = create_dict1(taint_var)
    dict2 = create_dict2(taint_var)
    dict3 = create_dict3(taint_var)

    # Pass the data to the sink
    sink1(dict1)
    sink2(dict2)
    sink3(dict3)


if __name__ == "__main__":
    main()