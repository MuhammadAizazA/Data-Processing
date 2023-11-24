def simple_read_data(): 
    text = []
    try:
        with open('data/text.txt', 'r') as f:
            text = [line.strip() for line in f.readlines()]
        print(text)
    except FileNotFoundError:
        print("The file 'text.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Execution Completed!")

def simple_write_data():
    text = ["abc is gone", "How are you doing?", "All is well"]
    try:
        with open('data/simple_text_file_created.txt', 'a') as f:
            for line in text:
                f.write(line + '\n')
    except Exception as e:
        print(f"An error Occurred: {e}")

if __name__=="__main__":
    simple_read_data()
    simple_write_data()