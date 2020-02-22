import os
import multiprocessing

if __name__ == '__main__':
    directory = os.path.dirname(os.path.abspath(__file__))
    this_file_name = os.path.basename(__file__)
    processes = list()

    for f in os.listdir(directory):
        if len(f) > 3 and f[-3:] == '.py' and f != this_file_name:
            
            with open(directory + '/' + f, 'r') as script:
                process = multiprocessing.Process(target=exec, args=(script.read(),))
                processes.append(process)
                process.start()

    for process in processes:
        process.join()
