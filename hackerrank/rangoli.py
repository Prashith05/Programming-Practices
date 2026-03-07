def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    # Create the pattern list
    lines = []
    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size-3, "-"))

    # Print the upper and lower parts
    print('\n'.join(lines[::-1] + lines[1:]))


# Example usage:
if __name__ == '__main__':
    n = int(input("Enter size: "))
    print_rangoli(n)
