
class Insta_Helpers:

    @staticmethod
    def change_username(username: str) -> None:
        fin = open("fetchUserFollowData.js", "rt")
        temp = []
        for line in fin:
            if(line.find('let username') != -1):
                line='let username = "'+username+'"\r\n'
            temp.append(line)
        
        fin.close()

        fout = open("fetchUserFollowData.js", "wt")

        for line in temp:
            fout.writelines(line)
        fout.close()

    @staticmethod
    def write_data_to_file(file_name: str, data_to_be_written: str) -> None:
        with open(file_name, 'w+') as file:
            file.writelines(data_to_be_written.replace(",",'\n'))
        file.close()