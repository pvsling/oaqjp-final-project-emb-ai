from emotion_detection import emotion_detector


def main(): 
    result = emotion_detector("I love this new technology.")

    with open("2b_application_creation.txt", "w") as file:
        file.write(result)

if __name__ == '__main__':
    main()