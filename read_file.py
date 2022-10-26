"""dosyadaki liste satırlarının bir listesini döndürür - bir listedeki her satırın tümü tek bir listede saklanır"""

def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)

    return lines_list
