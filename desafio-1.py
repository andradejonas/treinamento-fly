def solve(s):
    sequences = []
    current_sequence = ''

    for i in range(len(s)):
        char = s[i]

        if char.isdigit():
            current_sequence += char

        else:
            if current_sequence:
                sequences.append(int(current_sequence))
                current_sequence = ''
                
    if current_sequence:          
        sequences.append(int(current_sequence))

    return max(sequences)

#Exemplo
string = 'sjkdlenaibc873bhjs73bhei745b73b73gbd'
print(solve(string))


