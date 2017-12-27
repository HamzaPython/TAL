from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showerror, showwarning
from zipfile import *
import sys
from pathlib import Path, PurePath


def add_path():
    ''' recognize the algorithm's imports'''
    path_string = str(Path(__file__).resolve())
    current_path = PurePath(path_string)
    TAL_folder = current_path.parents[1]
    TAL_folder_string = str(TAL_folder)
    code_folder = TAL_folder.joinpath('Metrics_source_code')
    code_folder_string = str(code_folder)

    sys.path.append(code_folder_string)
    initialdir = TAL_folder_string
    return initialdir


add_path()
import fmeasure_score
import bleu_score
import nist_score
import wer_score

# def which_os():
#     import platform
#     os_name = platform.system()
#     if os_name == 'Linux':
#         sys.path.append('/home/hamza/Bureau/TAL/Metrics_source_code')
#         initialdir = "/home/hamza/Bureau"
#     elif os_name == 'Windows':
#         sys.path.append(r'C:\Users\Hamza\Desktop\TAL\Metrics_source_code')
#         initialdir = r"C:\Users\Hamza\Desktop"
#     return initialdir
# which_os()


class gui_class():
    def __init__(self, master, initialdir):
        ''' master (main window) '''
        self.master = master
        ''' initial directory '''
        self.initialdir = initialdir
        ''' frames to group widgets '''
        self.frame_1 = Frame(master=self.master, background="#A9F5A9")
        self.frame_2 = Frame(master=self.master, background="#A9F5A9")
        self.frame_3 = Frame(master=self.master, background="#A9F5A9")
        ''' frames for panding '''
        self.frame_padding_0 = Frame(
            master=self.master, height=20, background="#A9F5A9")
        self.frame_padding_1 = Frame(
            master=self.master, height=20, background="#A9F5A9")
        self.frame_padding_2 = Frame(
            master=self.master, height=20, background="#A9F5A9")
        self.frame_padding_3 = Frame(
            master=self.master, height=20, background="#A9F5A9")
        self.frame_ipadding_1 = Frame(
            master=self.frame_3, width=5, background="#A9F5A9")
        self.frame_ipadding_2 = Frame(
            master=self.frame_3, width=10, background="#A9F5A9")
        self.frame_ipadding_3 = Frame(
            master=self.frame_2, width=10, background="#A9F5A9")
        self.frame_ipadding_4 = Frame(
            master=self.frame_1, width=10, background="#A9F5A9")
        self.frame_ipadding_5 = Frame(
            master=self.frame_1, width=10, background="#A9F5A9")
        self.frame_ipadding_6 = Frame(
            master=self.frame_1, width=10, background="#A9F5A9")
        self.frame_ipadding_7 = Frame(
            master=self.frame_3, width=115, background="#A9F5A9")
        ''' widgets in frame_1 '''
        self.reference_label = Label(
            master=self.frame_1,
            text="references:",
            font="arial 12 bold",
            background="#A9F5A9")
        self.hypothesis_label = Label(
            master=self.frame_1,
            text="hypothesis:",
            font="arial 12 bold",
            background="#A9F5A9")
        self.path_reference = Entry(master=self.frame_1)
        self.path_hypothesis = Entry(master=self.frame_1)
        self.import_reference_button = Button(
            master=self.frame_1,
            text='...',
            height=1,
            width=1,
            command=lambda: self.importfile(self.path_reference, "reference"),
            font="system 10 bold")
        self.import_hypothesis_button = Button(
            master=self.frame_1,
            text='...',
            height=1,
            width=1,
            command=lambda: self.importfile(self.path_hypothesis, "hypothesis"),
            font="system 10 bold")
        self.clear_reference_button = Button(
            master=self.frame_1,
            text='Clear',
            command=lambda: self.clear(self.path_reference),
            font="system 10 bold")
        self.clear_hypothesis_button = Button(
            master=self.frame_1,
            text='Clear',
            command=lambda: self.clear(self.path_hypothesis),
            font="system 10 bold")
        ''' widgets in frame_2 '''
        self.radiobutton_title = Label(
            master=self.frame_2,
            text="Algorithms:",
            font="arial 12 bold",
            background="#A9F5A9")
        algorithms = {1: 'F-measure', 2: 'Bleu', 3: 'Nist', 4: 'Wer'}
        self.variable = IntVar()
        self.radiobutton_algorithms = []
        for key, value in algorithms.items():
            rb_algo = Radiobutton(
                master=self.frame_2,
                variable=self.variable,
                text=value,
                value=key,
                width=10,
                background="#A9F5A9")
            self.radiobutton_algorithms.append(rb_algo)
        ''' widgets in frame_3 '''
        self.calcul_button = Button(
            master=self.frame_3,
            text='Calcul score',
            command=self.calcul_score,
            font="system 10 bold")
        self.display_score = Label(
            master=self.frame_3,
            text="0",
            height=2,
            width=6,
            background="white",
            font="system 10 bold")
        self.clear_all_button = Button(
            master=self.frame_3,
            text='Clear all',
            command=self.clear_all,
            font="system 10 bold")
        ''' Display widgets '''
        # display frames:
        self.frame_padding_0.pack(fill=BOTH, side=TOP)
        self.frame_1.pack(fill=BOTH, side=TOP)
        self.frame_padding_1.pack(fill=BOTH, side=TOP)
        self.frame_2.pack(fill=BOTH, side=TOP)
        self.frame_padding_2.pack(fill=BOTH, side=TOP)
        self.frame_3.pack(fill=BOTH, side=TOP)
        self.frame_padding_3.pack(fill=BOTH, side=TOP)
        # display other widgets:
        # display widgets in frame_1:
        self.reference_label.grid(row=0, column=0, sticky=W, padx=4, pady=2)
        self.path_reference.grid(row=0, column=2)
        self.import_reference_button.grid(row=0, column=4, padx=2, pady=4)
        self.clear_reference_button.grid(row=0, column=6)
        self.hypothesis_label.grid(row=1, column=0, sticky=W, padx=4, pady=2)
        self.path_hypothesis.grid(row=1, column=2)
        self.import_hypothesis_button.grid(row=1, column=4, padx=2, pady=4)
        self.clear_hypothesis_button.grid(row=1, column=6)
        self.frame_ipadding_4.grid(rowspan=2, column=1)
        self.frame_ipadding_5.grid(rowspan=2, column=3)
        self.frame_ipadding_4.grid(rowspan=2, column=5)
        # display widgets in frame_2:
        self.radiobutton_title.pack(side=LEFT)
        self.frame_ipadding_3.pack(side=LEFT)
        for radiobutton in self.radiobutton_algorithms:
            radiobutton.pack(side=LEFT)
        # display widgets in frame_3:
        self.frame_ipadding_7.pack(side=LEFT)
        self.calcul_button.pack(side=LEFT)
        self.frame_ipadding_1.pack(side=LEFT)
        self.display_score.pack(side=LEFT)
        self.frame_ipadding_2.pack(side=LEFT)
        self.clear_all_button.pack(side=LEFT)

    def importfile(self, path_cell, type):
        ''' import references and hypothesis files '''
        path_name = filedialog.askopenfilename(
            initialdir=self.initialdir,
            title="Select {} file".format(type),
            filetypes=(("text files", "*.txt"), ("zip files", "*.zip")))
        # , ("all files", "*")
        path_cell.insert(0, path_name)
        path_cell.configure(state='readonly')

    def open_references_hypothesis(self):
        ''' extract text from references and hypothesis files '''
        while True:
            references = []
            path_reference_string = self.path_reference.get()
            if is_zipfile(path_reference_string):
                try:
                    with ZipFile(path_reference_string) as my_zipfile:
                        for txtfile in my_zipfile.namelist():
                            try:
                                with my_zipfile.open(txtfile) as f:
                                    file_data = f.read().decode('utf-8')
                                    references.append(file_data)
                            except IOError:
                                showerror("Error", "Please use valide files")
                                self.importfile(self.path_reference,
                                                "reference")
                            else:
                                break
                except (BadZipFile, LargeZipFile):
                    showerror("Error", "Please use valide zip")
                    self.importfile(self.path_reference, "reference")
                else:
                    break
            else:
                try:
                    with open(path_reference_string) as f:
                        file_data = str(f.read())
                        references.append(file_data)
                except IOError:
                    showerror("Error", "Please use valide file")
                    self.importfile(self.path_reference, "reference")
                else:
                    break

        while True:
            path_hypothesis_string = self.path_hypothesis.get()
            if is_zipfile(path_hypothesis_string):
                try:
                    with ZipFile(path_hypothesis_string) as my_zipfile:
                        files = my_zipfile.namelist()
                        nb_files = len(files)
                        if nb_files > 1:
                            showerror("Error",
                                      "There is more then 1 hypothesis file!!")
                            self.importfile(self.path_hypothesis, "hypothesis")
                        else:
                            try:
                                with my_zipfile.open(txtfile) as f:
                                    hypothesis = f.read().decode('utf-8')
                            except IOError:
                                showerror("Error", "Please use valide files")
                                self.importfile(self.path_hypothesis,
                                                "hypothesis")
                            else:
                                break
                except (BadZipFile, LargeZipFile):
                    showerror("Error", "Please use valide zip")
                    self.importfile(self.path_hypothesis, "hypothesis")
                else:
                    break

            else:
                try:
                    with open(path_hypothesis_string) as f:
                        hypothesis = f.read()
                except IOError:
                    showerror("Error", "Please use valide file")
                    self.importfile(self.path_hypothesis, "hypothesis")
                else:
                    break
        return references, hypothesis

    def calcul_score(self):
        references, hypothesis = self.open_references_hypothesis()
        v = self.variable.get()
        if v == 1:
            f = fmeasure_score.fmeasure_score_class(hypothesis, *references)
            score = f.calculate_fmesure_score()
        elif v == 2:
            b = bleu_score.bleu_score_class(hypothesis, *references)
            score = b.calculate_bleu_score()
        elif v == 3:
            n = nist_score.nist_score_class(hypothesis, *references)
            score = n.calculate_nist_score()
        elif v == 4:
            w = wer_score.wer_score_class(hypothesis, *references)
            score = w.calculate_wer_score()
        else:
            showwarning("Warning", "You must choose one of the algorithms")
            score = 0
        self.display_score.configure(text=str(round(score, 2)))

    def clear(self, path_cell):
        ''' clear path_reference and path_hypothesis labels '''
        path_cell.configure(state=NORMAL)
        path_cell.delete(0, END)

    def clear_all(self):
        ''' clear path_reference, path_hypothesis and display_score labels '''
        self.clear(self.path_reference)
        self.clear(self.path_hypothesis)
        self.display_score.configure(text="0")


def main():
    root = Tk()
    root.title("Notre Application")
    root.geometry("500x200+350+50")
    app = gui_class(root, add_path())
    root.mainloop()


main()
