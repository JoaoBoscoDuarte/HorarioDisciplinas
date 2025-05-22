import threading
import time
import sys

def with_loading(task_function, *args, message="Loading", **kwargs):
    
    """
    Runs a task function while displaying a loading animation.
    :param task_function: The function to run.
    :param args: Positional arguments for the function.
    :param message: Optional loading message.
    :param kwargs: Keyword arguments for the function.
    :return: The result of the task_function.
    """

    stop_event = threading.Event()

    def loading_animation():
        chars = "|/-\\"
        idx = 0
        while not stop_event.is_set():
            sys.stdout.write(f"\r{message}... {chars[idx % len(chars)]}")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)
        sys.stdout.write("\rDone!            \n")

    thread = threading.Thread(target=loading_animation)
    thread.start()

    try:
        result = task_function(*args, **kwargs)
        
    finally:
        stop_event.set()
        thread.join()

    return result
