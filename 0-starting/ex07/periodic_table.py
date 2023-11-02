
def print_haeders():
    print("<!DOCTYPE html> \n\
          <html lang=\"en\"> \n\
          <head> \n\
          \t<meta charset=\"UTF-8\"> \n\
          \t<title>Periodic Table</title> \n\
          </head> \n\
                    \
          <body> \n\
          \t<table>")

def print_footers():
    print("\t</table>")
    print("</body>")
    print("</html>")

def periodic_table():

    try:
        file = open('periodic_table.txt', 'r')
    except FileNotFoundError:
        print('File not found')
        exit(1)


    for i in range(9):
        print("\t\t<tr>")
        j = 0
        while j < 18:
            line = file.readline()
            if line == '':
                break
            line = line.split('=')
            name = line[0]
            properties = line[1].split(',')
            number = int(properties[0].split(':')[1])
            while number != j and j < 18:
                print("\t\t\t<td style=\"border: 1px solid black; padding: 10px;\">")
                print("\t\t\t</td>")
                j += 1
            print("\t\t\t<td style=\"border: 1px solid black; padding: 10px;\">")
            print("\t\t\t\t<h4>" + name + "</h4>")
            print("\t\t\t\t<ul>")
            for prop in properties:
                print("\t\t\t\t\t<li>" + prop.strip() + "</li>")
            print("\t\t\t\t</ul>")
            print("\t\t\t</td>")
            j += 1
        print("\t\t</tr>")



if __name__ == '__main__':
    print_haeders()
    periodic_table()
    print_footers()
