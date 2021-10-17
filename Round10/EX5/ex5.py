import re

class Analize:

    def __init__(self, text_name):
        self._get_data(text_name)
        self.textName = text_name


    def _get_data(self, text_name):
        with open(text_name, "r") as f:
            data = f.read().replace("\n", "")
        self.data = data


    def amount_signs(self):
        return len(self.data)

    def amount_of_lines(self):
        with open(self.textName) as f:
            line_count = 0
            for line in f:
                line_count += 1
        return line_count

    def amount_of_words(self):
        new_A = []
        with open(self.textName, "r") as f:
            for line in f:
                line = re.sub(r"[^\w\s]", "", line)
                line = re.sub(r'\d', "", line)
                new_A += line.split()
        return len(new_A)

    def amount_of_substrings(self, substring):
        return( len(self.find_kr(substring)))

    def find_kr(self, substring: str):
        out = []
        text_l = len(self.data)
        substring_l = len(substring)
        ALF = 40999999
        PR_N = 3571
        MO = pow(ALF, substring_l - 1) % PR_N
        text_h = 0
        substring_h = 0
        for i in range(substring_l):
            text_h = (ALF * text_h + ord(self.data[i])) % PR_N
            substring_h = (ALF * substring_h + ord(substring[i])) % PR_N

        for i in range(text_l - substring_l + 1):
            j = 0
            if text_h == substring_h:
                while j < substring_l and substring[j] == self.data[i + j]:
                    j += 1
                if j == substring_l:
                    out.append(i + 1)
            if i < text_l - substring_l:
                text_h = (text_h - MO * ord(self.data[i])) % PR_N
                text_h = (text_h * ALF + ord(self.data[i + substring_l])) % PR_N
                text_h = (text_h + PR_N) % PR_N
        return out


    def _check(self, substring: str):
        text_l = len(self.data)
        substring_l = len(substring)
        if text_l < substring_l or text_l == 0 or substring_l == 0:
            return True

analize = Analize("PiKNik/Round10/EX5/pan-tadeusz.txt")


print(analize.amount_signs())
print(analize.amount_of_words())
print(analize.amount_of_lines())
print(analize.amount_of_substrings('int'))