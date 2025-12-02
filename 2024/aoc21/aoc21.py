from itertools import permutations
from rich import print

def generate_num_commands(code):
    # Define the keypad layout
    keypad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2)
    }

    # Start at the initial position 'A'
    current_position = keypad['A']
    all_sequences = []

    def generate_combinations(start, end):
        vertical_moves = end[0] - start[0]
        horizontal_moves = end[1] - start[1]

        vertical_command = ['v'] * vertical_moves if vertical_moves > 0 else ['^'] * abs(vertical_moves)
        horizontal_command = ['>'] * horizontal_moves if horizontal_moves > 0 else ['<'] * abs(horizontal_moves)

        movement_combinations = permutations(vertical_command + horizontal_command)

        # Filter out any combinations that pass through the gap
        valid_combinations = set()
        for combination in movement_combinations:
            current_position = list(start)
            is_valid = True
            for move in combination:
                if move == 'v':
                    current_position[0] += 1
                elif move == '^':
                    current_position[0] -= 1
                elif move == '>':
                    current_position[1] += 1
                elif move == '<':
                    current_position[1] -= 1

                # Check if the current position is the gap
                if tuple(current_position) == (3, 0):
                    is_valid = False
                    break

            if is_valid:
                valid_combinations.add(combination)

        # If no valid combinations exist, raise an error
        if not valid_combinations:
            raise ValueError("No valid path exists that avoids the gap.")

        return valid_combinations

    for char in code:
        target_position = keypad[char]
        movement_combinations = generate_combinations(current_position, target_position)

        if not all_sequences:
            # Initialize with the first set of movements
            all_sequences = [[*movement, 'A'] for movement in movement_combinations]
        else:
            # Extend each existing sequence with new movements
            new_sequences = []
            for sequence in all_sequences:
                for movement in movement_combinations:
                    new_sequences.append(sequence + [*movement, 'A'])
            all_sequences = new_sequences

        current_position = target_position

    # Convert each sequence to a string
    return [''.join(sequence) for sequence in all_sequences]

def generate_dir_commands(sequence):
    # Define the directional keypad layout
    keypad = {
        'A': (0, 2),  # Activate button
        '^': (0, 1),  # Up button
        '/': (0, 0),  # Gap
        '<': (1, 0),  # Left button
        'v': (1, 1),  # Down button
        '>': (1, 2)   # Right button
    }

    # Start at the initial position 'A'
    current_position = keypad['A']
    all_sequences = [[]]  # Start with an empty sequence

    for char in sequence:
        target_position = keypad[char]

        # Calculate vertical and horizontal movements
        vertical_moves = target_position[0] - current_position[0]
        horizontal_moves = target_position[1] - current_position[1]

        vertical_command = ['v'] * vertical_moves if vertical_moves > 0 else ['^'] * abs(vertical_moves)
        horizontal_command = ['>'] * horizontal_moves if horizontal_moves > 0 else ['<'] * abs(horizontal_moves)

        movement_combinations = permutations(vertical_command + horizontal_command)

        # Filter out any combinations that pass through the gap
        valid_combinations = set()
        for combination in movement_combinations:
            current_pos = list(current_position)
            is_valid = True
            for move in combination:
                if move == 'v':
                    current_pos[0] += 1
                elif move == '^':
                    current_pos[0] -= 1
                elif move == '>':
                    current_pos[1] += 1
                elif move == '<':
                    current_pos[1] -= 1

                # Check if the current position is the gap
                if tuple(current_pos) == (0, 0):
                    is_valid = False
                    break

            if is_valid:
                valid_combinations.add(combination)

        # Extend all existing sequences with the new valid combinations
        new_sequences = []
        for seq in all_sequences:
            for movement in valid_combinations:
                new_sequences.append(seq + list(movement) + ['A'])
        all_sequences = new_sequences

        # Update current position
        current_position = target_position

    return [''.join(sequence) for sequence in all_sequences]

def avoids_gap(sequence):
    # Define the directional keypad layout
    keypad = {
        'A': (0, 2),  # Activate button
        '^': (0, 1),  # Up button
        '/': (0, 0),  # Gap
        '<': (1, 0),  # Left button
        'v': (1, 1),  # Down button
        '>': (1, 2)   # Right button
    }

    # Start at the initial position 'A'
    current_position = keypad['A']

    for move in sequence:
        if move == 'v':
            current_position = (current_position[0] + 1, current_position[1])
        elif move == '^':
            current_position = (current_position[0] - 1, current_position[1])
        elif move == '>':
            current_position = (current_position[0], current_position[1] + 1)
        elif move == '<':
            current_position = (current_position[0], current_position[1] - 1)

        # Check if the current position is the gap
        if current_position == (0, 0):
            return False

    return True

def calculate_len(command):
    # calculate the length of the direction keyboard command
    # needed to produce input command
    # use the same directional keyboard layout like in the function
    # generate_dir_commands
    # to produce the command

    # Define the directional keypad layout
    keypad = {
        'A': (0, 2),  # Activate button
        '^': (0, 1),  # Up button
        '/': (0, 0),  # Gap
        '<': (1, 0),  # Left button
        'v': (1, 1),  # Down button
        '>': (1, 2)   # Right button
    }
    # Start at the initial position 'A'
    current_position = keypad['A']
    maxlen = 0
    for char in command:
        target_position = keypad[char]

        # Calculate vertical and horizontal movements
        vertical_moves = target_position[0] - current_position[0]
        horizontal_moves = target_position[1] - current_position[1]
        maxlen += abs(vertical_moves) + abs(horizontal_moves)
        # change current position to target position
        current_position = target_position
    return maxlen

codes = ['149A', '582A', '540A', '246A', '805A']
result = 0

for code in codes:
    # Generate initial commands
    initial_commands = generate_num_commands(code)
    print("Initial Commands:", initial_commands)

    # Find the shortest commands at each level
    def find_shortest_commands(commands):
        shortest_length = float('inf')
        shortest_commands = []

        for command in commands:
            command_length = calculate_len(command)
            if command_length < shortest_length:
                shortest_length = command_length
                shortest_commands = [command]
            elif command_length == shortest_length:
                shortest_commands.append(command)

        return shortest_commands

    # First level
    shortest_commands = find_shortest_commands(initial_commands)

    # Second level
    refined_commands = []
    for command in shortest_commands:
        refined_commands.extend(generate_dir_commands(command))
    shortest_commands = find_shortest_commands(refined_commands)

    # Third level
    final_commands = []
    for command in shortest_commands:
        final_commands.extend(generate_dir_commands(command))
    shortest_commands = find_shortest_commands(final_commands)

    # Calculate result for the current code
    numeric_part = int(''.join(filter(str.isdigit, code)))
    result += numeric_part * len(shortest_commands[0])
    print(f"Code: {code}, Shortest Command Length: {len(shortest_commands[0])}")

print("Final Result:", result)

