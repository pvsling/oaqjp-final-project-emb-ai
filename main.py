from emotion_detection import emotion_detector


def main2b(): 
    result = emotion_detector("I love this new technology.")

    with open("2b_application_creation.txt", "w") as file:
        file.write(result)

def main3(): 
    result = emotion_detector("I am so happy I am doing this.")
    with open("3b_formatted_output_test.txt", "w") as file:
        file.write(str(result))

if __name__ == '__main__':
    main3()