import pip, os, sys
   

try:
    from tqdm import tqdm
except:
    print("Package 'tqdm' isn't installed. Installation process will begin soon")
    pip.main(['install', 'tqdm'])
    sys.exit("Package installation process is completed. Please relaunch this script")


# get all extension available in current directory
files = [file for file in os.listdir('.') if os.path.isfile(os.path.join('.', file))]
extension_list = set()
for file in files:
    extension = file.split(".")[1]
    if (extension not in extension_list and extension != "exe"):
        extension_list.add(extension)     
extension_list = list(extension_list)
matched_files =[file for file in files if file.split(".")[1] == "extension_list[extension_index]"]
#user interface
print("MASS FILE DELETING TOOL".center(50, " "))
print("To Van Hien".center(50, "-"))
print("Oct 25, 2022 - Victoria, Canada".center(50, "-"))
print("Choose language:\n1.English\n2.Tiếng Việt")
language = input ("-->")
confirmation = ""
if language == "1" :
    while confirmation == "":
        print("In current directory, there are " + str(len(extension_list)) + " different file extensions")
        for i in range(len(extension_list)):
            print(i+1, ": ", extension_list[i])
        while (1>0):
            extension_index = input("Which file extension you want to remove? Press Enter to exit program\n-->")
            if (extension_index == ""):
                sys.exit()
            if extension_index.isnumeric():
                extension_index = int(extension_index)-1
                if extension_index < 0 or extension_index > len(extension_list):
                    print("Please choose a number between 1 and", len(extension_list), "corresponding to the file extension you want to remove above")
                else:
                    break
            else:
                print("Please type a number only")
        matched_files =[file for file in files if file.split(".")[1] == extension_list[extension_index]]
        confirmation = input("There are " + str(len(matched_files)) + " matched the file extension " + extension_list[extension_index] +". Type \"Confirm\" to confirm. Press Enter to abort\n-->")
    if confirmation == "Confirm":
        print("Start deleting all files with extension " + extension_list[extension_index])
        for i in tqdm(range(len(matched_files))):
            os.remove(matched_files[i])
        input("Finished! Press Enter to exit program\n-->")
if language == "2" :
    while confirmation == "":
        print("Trong thư mục hiện tại, có tất cả " + str(len(extension_list)) + " định dạng khác nhau" )
        for i in range(len(extension_list)):
            print(i+1, ": ", extension_list[i])
        while (1>0):
            extension_index = input("Bạn muốn xóa file có định dạng nào? Nhấn Enter để thoát chương trình\n-->")
            if (extension_index == ""):
                sys.exit()
            if extension_index.isnumeric():
                extension_index = int(extension_index)-1
                if extension_index < 0 or extension_index > len(extension_list):
                    print("Hãy lựa một số giữa 1 và", len(extension_list), "tương ứng với định dạng bạn muốn xóa ở trên")
                else:
                    break
            else:
                print("Chỉ chấp nhận số tự nhiên")
        matched_files =[file for file in files if file.split(".")[1] == extension_list[extension_index]]
        confirmation = input("Có tất cả " + str(len(matched_files)) + " tệp mang định dạng " + extension_list[extension_index] +". Nhập \"OK\" để xác nhận. Nhấn Enter để thoát chương trình\n-->")
    if confirmation == "OK":
        print("Bắt đầu xóa tất cả tệp có định dạng " + extension_list[extension_index])
        for i in tqdm(range(len(matched_files))):
            os.remove(matched_files[i])
        input("Hoàn tất! Nhấn Enter để thoát\n-->")
