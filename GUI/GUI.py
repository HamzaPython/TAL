from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showerror, showwarning
from zipfile import *
import sys
import platform


def which_os():
    os_name = platform.system()
    if os_name == 'Linux':
        sys.path.append('/home/hamza/Bureau/TAL/Metrics_source_code')
        initialdir = "/home/hamza/Bureau"
    elif os_name == 'Windows':
        sys.path.append('/home/hamza/Bureau/TAL/Metrics_source_code')
        initialdir = "/home/hamza/Bureau"
    return initialdir


which_os()
import fmeasure_score
import bleu_score
import nist_score


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
        self.hypothese_label = Label(
            master=self.frame_1,
            text="hypothese:",
            font="arial 12 bold",
            background="#A9F5A9")
        self.path_reference = Entry(master=self.frame_1)
        self.path_hypothese = Entry(master=self.frame_1)
        self.import_reference_button = Button(
            master=self.frame_1,
            text='...',
            height=1,
            width=1,
            command=lambda: self.importfile(self.path_reference, "reference"),
            font="system 10 bold")
        self.import_hypothese_button = Button(
            master=self.frame_1,
            text='...',
            height=1,
            width=1,
            command=lambda: self.importfile(self.path_hypothese, "hypothese"),
            font="system 10 bold")
        self.clear_reference_button = Button(
            master=self.frame_1,
            text='Clear',
            command=lambda: self.clear(self.path_reference),
            font="system 10 bold")
        self.clear_hypothese_button = Button(
            master=self.frame_1,
            text='Clear',
            command=lambda: self.clear(self.path_hypothese),
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
        ## display widgets in frame_1:
        self.reference_label.grid(row=0, column=0, sticky=W, padx=4, pady=2)
        self.path_reference.grid(row=0, column=2)
        self.import_reference_button.grid(row=0, column=4, padx=2, pady=4)
        self.clear_reference_button.grid(row=0, column=6)
        self.hypothese_label.grid(row=1, column=0, sticky=W, padx=4, pady=2)
        self.path_hypothese.grid(row=1, column=2)
        self.import_hypothese_button.grid(row=1, column=4, padx=2, pady=4)
        self.clear_hypothese_button.grid(row=1, column=6)
        self.frame_ipadding_4.grid(rowspan=2, column=1)
        self.frame_ipadding_5.grid(rowspan=2, column=3)
        self.frame_ipadding_4.grid(rowspan=2, column=5)
        ## display widgets in frame_2:
        self.radiobutton_title.pack(side=LEFT)
        self.frame_ipadding_3.pack(side=LEFT)
        for radiobutton in self.radiobutton_algorithms:
            radiobutton.pack(side=LEFT)
        ## display widgets in frame_3:
        self.frame_ipadding_7.pack(side=LEFT)
        self.calcul_button.pack(side=LEFT)
        self.frame_ipadding_1.pack(side=LEFT)
        self.display_score.pack(side=LEFT)
        self.frame_ipadding_2.pack(side=LEFT)
        self.clear_all_button.pack(side=LEFT)

    def importfile(self, path_cell, type):
        ''' import references and hypothese files '''
        path_name = filedialog.askopenfilename(
            initialdir=self.initialdir,
            title="Select {} file".format(type),
            filetypes=(("text files", "*.txt"), ("zip files", "*.zip")))
        # , ("all files", "*")
        path_cell.insert(0, path_name)
        path_cell.configure(state='readonly')

    def open_references_hypothese(self):
        ''' extract text from references and hypothese files '''
        while True:
            references = []
            path_reference_string = self.path_reference.get()
            if is_zipfile(path_reference_string):
                try:
                    with zipfile(path_reference_string) as my_zipfile:
                        for txtfile in my_zipfile.namelist():
                            try:
                                with my_zipfile.open(txtfile) as f:
                                    file_data = f.read()
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
                        file_data = f.read()
                        references.append(file_data)
                except IOError:
                    showerror("Error", "Please use valide file")
                    self.importfile(self.path_reference, "reference")
                else:
                    break

        while True:
            path_hypothese_string = self.path_hypothese.get()
            if is_zipfile(path_hypothese_string):
                try:
                    with zipfile(path_hypothese_string) as my_zipfile:
                        files = my_zipfile.namelist()
                        nb_files = len(files)
                        if nb_files > 1:
                            showerror("Error",
                                      "There is more then 1 hypothese file!!")
                            self.importfile(self.path_hypothese, "hypothese")
                        else:
                            try:
                                with my_zipfile.open(txtfile) as f:
                                    hypothese = f.read()
                            except IOError:
                                showerror("Error", "Please use valide files")
                                self.importfile(self.path_hypothese,
                                                "hypothese")
                            else:
                                break
                except (BadZipFile, LargeZipFile):
                    showerror("Error", "Please use valide zip")
                    self.importfile(self.path_hypothese, "hypothese")
                else:
                    break

            else:
                try:
                    with open(path_hypothese_string) as f:
                        hypothese = f.read()
                except IOError:
                    showerror("Error", "Please use valide file")
                    self.importfile(self.path_hypothese, "hypothese")
                else:
                    break
        return references, hypothese

    def calcul_score(self):
        references, hypothese = self.open_references_hypothese()
        v = self.variable.get()
        if v == 1:
            f = fmeasure_score.fmeasure_score_class(hypothese, *references)
            score = f.calculate_fmesure_score()
        elif v == 2:
            b = bleu_score.bleu_score_class(hypothese, *references)
            score = b.calculate_bleu_score()
        elif v == 3:
            n = nist_score.nist_score_class(hypothese, *references)
            score = n.calculate_nist_score()
        elif v == 4:
            pass  #WER
        else:
            showwarning("Warning", "You must choose one of the algorithms")
            score = 0
        self.display_score.configure(text=str(round(score, 2)))

    def clear(self, path_cell):
        ''' clear path_reference and path_hypothese labels '''
        path_cell.configure(state=NORMAL)
        path_cell.delete(0, END)

    def clear_all(self):
        ''' clear path_reference, path_hypothese and display_score labels '''
        self.clear(self.path_reference)
        self.clear(self.path_hypothese)
        self.display_score.configure(text="0")


def main():
    root = Tk()
    root.title("Notre Application")
    root.geometry("500x200+350+50")
    root.configure(background="white")
    app = gui_class(root, which_os())
    root.mainloop()


main()
