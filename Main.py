import subprocess


# This function extracts commands and directory addresses from user input
import time


def input_separator(user_input):
    user_input = user_input.rstrip("}")
    user_input = user_input.lstrip("{")
    commands = user_input.split(">, ")
    output_commands = []
    i = 0
    while i < len(commands) - 1:
        command = commands[i]
        command = command.lstrip("<")
        single_command_list = command.split(", ")
        for j in single_command_list:
            output_commands.append(j)
        i += 1

    output_file_location = commands[len(commands) - 1]
    output_file_location = output_file_location.lstrip("<")
    output_file_location = output_file_location.rstrip(">")
    output_commands.append(output_file_location)
    return output_commands


# This function terminates three generated dockers
def dockers_terminator():
    print("Terminating dockers...")
    subprocess.run("docker stop container1")
    subprocess.run("docker rm container1")
    subprocess.run("docker stop container2")
    subprocess.run("docker rm container2")
    subprocess.run("docker stop container3")
    subprocess.run("docker rm container3")
    print("All dockers terminated")






# Main part of the code starts here
print("Creating container1, container2 and container3...")
subprocess.run("docker run -t -d --name container1 cloud_computing_image")
subprocess.run("docker run -t -d --name container2 cloud_computing_image")
subprocess.run("docker run -t -d --name container3 cloud_computing_image")

user_id = 1

while True:
    user_input = input("Input: ")
    if user_input == "exit":
        dockers_terminator()
        break

    else:
        commands_list = input_separator(user_input)
        commands_string = "docker exec container1 python /home/cloud_computing/Script.py "
        for i in commands_list:
            commands_string += i + " "
        commands_string = commands_string.rstrip(" ")
        start_time = time.time()
        # making the output directory in the container
        subprocess.run("docker exec container1 mkdir -p /home/cloud_computing/Output/user" + str(user_id) + "_output")
        subprocess.run("docker exec container1 touch /home/cloud_computing/Output/user" + str(user_id) + "_output" + "/min.txt")
        subprocess.run("docker exec container1 touch /home/cloud_computing/Output/user" + str(user_id) + "_output" + "/max.txt")
        subprocess.run("docker exec container1 touch /home/cloud_computing/Output/user" + str(user_id) + "_output" + "/average.txt")
        subprocess.run("docker exec container1 touch /home/cloud_computing/Output/user" + str(user_id) + "_output" + "/sort.txt")
        subprocess.run("docker exec container1 touch /home/cloud_computing/Output/user" + str(user_id) + "_output" + "/wordcount.txt")
        commands_string += "/user" + str(user_id) + "_output"
        print("The command is: " + commands_string)
        user_id += 1
        subprocess.run(commands_string)
        stop_time = time.time()
        print("Time: " + str(round(stop_time - start_time, 2)) + " s")














