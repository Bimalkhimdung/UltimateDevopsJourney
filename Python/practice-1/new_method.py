class main(object):
    def __new__(cls):
        print("new method called")
        return super(main, cls).__new__(cls)
    def __init__(self):
        print("Init method called")



if __name__ == "__main__":
    main()