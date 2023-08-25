ecg_values = [0.5, 0.8, 1.2, 0.9, 0.6, 0.7, 1.3, 1.1, 0.7, 0.4, 1.4, 1.2, 0.9, 0.6, 0.8, 1.2, 1.1, 0.7]

heartbeats = []
for i, value in enumerate(ecg_values):
    if value >= 1.0:  # Assuming a threshold of 1 to identify heartbeats
        heartbeats.append(i)

selected_indices = []
current_group = [heartbeats[0]]
for i in range(1, len(heartbeats)):
    if heartbeats[i] - heartbeats[i-1] == 1:
        current_group.append(heartbeats[i])
    else:
        selected_indices.append(max(current_group, key=lambda x: ecg_values[x]))
        current_group = [heartbeats[i]]

# Add the last group of indices
selected_indices.append(max(current_group, key=lambda x: ecg_values[x]))

lengths = []
for i in range(len(selected_indices) - 1):
    length = selected_indices[i+1] - selected_indices[i]
    lengths.append(length)

max_length = max(lengths)
min_length = min(lengths)



def calculate_heartbeats(i, ecg_list):
    ecg_values = ecg_list[i:i+100]

    heartbeats = []
    for i, value in enumerate(ecg_values):
        if value >= 1.0:  # Assuming a threshold of 1 to identify heartbeats
            heartbeats.append(i)

    selected_indices = []
    current_group = [heartbeats[0]]
    for i in range(1, len(heartbeats)):
        if heartbeats[i] - heartbeats[i-1] == 1:
            current_group.append(heartbeats[i])
        else:
            selected_indices.append(max(current_group, key=lambda x: ecg_values[x]))
            current_group = [heartbeats[i]]

    # Add the last group of indices
    selected_indices.append(max(current_group, key=lambda x: ecg_values[x]))

    lengths = []
    for i in range(len(selected_indices) - 1):
        length = selected_indices[i+1] - selected_indices[i]
        lengths.append(length)

    max_length = max(lengths)
    min_length = min(lengths)

    return max_length, min_length


