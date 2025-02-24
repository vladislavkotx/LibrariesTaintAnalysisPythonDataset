from config import get_user_input, configure_environment
from data_processing import create_list1, create_list2, create_list3, create_list4, create_list5
from utils import sink1, sink2, sink3, sink4, sink5


def main():
    # Configure the environment
    configure_environment()

    # Get tainted variable from user input
    taint_var = get_user_input()

    # Create lists and process data
    list1 = create_list1(taint_var)
    list2 = create_list2(taint_var)
    list3 = create_list3(taint_var)
    list4 = create_list4(taint_var)
    list5 = create_list5(taint_var)

    # Pass the data to the sink
    sink1(list1)
    sink2(list2)
    sink3(list3)
    sink4(list4)
    sink5(list5)


if __name__ == "__main__":
    main()