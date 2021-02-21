def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None
    nick_word_count = 0
    nick_sticker_count = 0
    nick_photo = 0
    erin_word_count = 0
    erin_sticker_count = 0
    erin_photo = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Nick':
            if s[2] == '貼圖':
                nick_sticker_count += 1
            elif s[2] == '圖片':
                nick_photo += 1
            else:
                for m in (s[2:]):
                    nick_word_count += len(m)
        elif name == 'Erin':
            if s[2] == '貼圖':
                erin_sticker_count += 1
            elif s[2] == '圖片':
                erin_photo += 1
            else:
                for m in (s[2]):
                    erin_word_count += len(m)
    print('Nick說了', nick_word_count, '個字', '傳了', nick_sticker_count, '個貼圖', nick_photo, '張圖片')
    print('Erin說了', erin_word_count, '個字', '傳了', erin_sticker_count, '個貼圖', erin_photo, '張圖片')


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('[LINE]Erin.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()
