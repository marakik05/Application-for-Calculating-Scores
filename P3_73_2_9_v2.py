from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QComboBox,  
QDesktopWidget, QScrollArea,  QWidget, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

import sys
import numpy as np
import pandas as pd

class NoWheelComboBox(QComboBox):
    def wheelEvent(self,event):
        event.ignore()
        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μοριοδότηση Παρέμβασης Π3-73-2.9")
        
        self.resize(1200,800)
        
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(False) 
      
        content = QWidget()
        content.setMinimumSize(1600, 1200)
        
               
        self.validator = QDoubleValidator(self)
        self.validator.setNotation(QDoubleValidator.StandardNotation)
      
        #Πλαίσιο προϋπολογισμού
        self.budget=QLabel(content)
        self.budget.setText("Προϋπολογισμός")
        self.budget.move(770,0)
        
        
        self.input_budget=QLineEdit(content)
        self.input_budget.move(860,0)
        self.input_budget.setAlignment(Qt.AlignCenter)
        self.input_budget.setValidator(self.validator)
        self.input_budget.textChanged.connect(self.simmetoxi_pososto)
        self.input_budget.textChanged.connect(self.critiria_moria_6_a)        
        self.input_budget.textChanged.connect(self.poso_ktiriaka_pososto)
        self.input_budget.textChanged.connect(self.critiria_moria_10)
        self.input_budget.textChanged.connect(self.poso_eksixronismos_pososto)
        self.input_budget.textChanged.connect(self.critiria_moria_11)
        self.input_budget.textChanged.connect(self.poso_ape_pososto)
        self.input_budget.textChanged.connect(self.critiria_moria_12)
        self.input_budget.textChanged.connect(self.epilex_budget)
        
        self.onoma_title=QLabel(content)
        self.onoma_title.setText("Ονοματεπώνυμο")
        self.onoma_title.move(515,0)
        
        
        self.onoma=QLineEdit(content)
        self.onoma.move(600,0)
        self.onoma.setAlignment(Qt.AlignCenter)
        
        #Κριτήρια επιλογής ξεκινώντας με τη σειρά από το κριτήριο 1 μέχρι και το 13
        self.criteria_1=QLabel(content)
        self.criteria_1.setText('1. Kατοχή της ιδιότητας του επαγγελματία γεωργού')
        self.criteria_1.move(10,30)
        self.criteria_1.adjustSize() 
        
        self.combo_1 = NoWheelComboBox(content)
        self.combo_1.addItems(["Επιλέξτε","Ναι", "Όχι"])
        self.combo_1.move(600,30)
        self.combo_1.currentIndexChanged.connect(self.critiria_moria_1)
        self.combo_1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        
        self.moria_1=QLineEdit(content)
        self.moria_1.setAlignment(Qt.AlignCenter)
        self.moria_1.setReadOnly(True) 
        self.moria_1.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.moria_1.move(860,30)

        self.moria_1.textChanged.connect(self.sum_total_moria)
        
        self.criteria_2=QLabel(content)
        self.criteria_2.setText('2. H προέλευση των ακαθάριστων εσόδων από την γεωργία είναι σημαντικά μεγαλύτερη από αυτή άλλων τομέων (>70%)')
        self.criteria_2.move(10,80)
        self.criteria_2.adjustSize() 
        
        self.esoda_agro=QLineEdit(content)
        self.esoda_agro.setAlignment(Qt.AlignCenter)         
        self.esoda_agro.move(600,80)
        self.esoda_agro.textChanged.connect(self.critiria_moria_2)
        self.esoda_agro.textChanged.connect(self.esoda_pososto)
        self.esoda_agro.setValidator(self.validator)
        
        self.esoda_agro_title=QLabel(content)
        self.esoda_agro_title.setText("Αγροτικά Έσοδα")
        self.esoda_agro_title.move(600,60)
        
        
        self.esoda=QLineEdit(content)
        self.esoda.setAlignment(Qt.AlignCenter)         
        self.esoda.move(600,130)
        self.esoda.textChanged.connect(self.critiria_moria_2)
        self.esoda.textChanged.connect(self.esoda_pososto)
        self.esoda.setValidator(self.validator)
        
        self.esoda_title=QLabel(content)
        self.esoda_title.setText("Συνολικά Έσοδα")
        self.esoda_title.move(600,110)
        
        self.esoda_pososto=QLineEdit(content)
        self.esoda_pososto.setAlignment(Qt.AlignCenter)         
        self.esoda_pososto.move(730,80)
        self.esoda_pososto.setReadOnly(True)
        self.esoda_pososto.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        
                  
        self.moria_2=QLineEdit(content)
        self.moria_2.setAlignment(Qt.AlignCenter)
        self.moria_2.setReadOnly(True) 
        self.moria_2.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_2.move(860,80)
        self.moria_2.textChanged.connect(self.sum_total_moria)
                
        
        self.criteria_3=QLabel(content)
        self.criteria_3.setText('3. Αξιολογείται και βαθμολογείται το οικονομικό μέγεθος της εκμετάλλευσης στην υφιστάμενη κατάσταση σε όρους \n τυπικής απόδοσης. Επιλέξτε την τυπική απόδοση της εκμετάλλευσης το έτος 2024')
        self.criteria_3.move(10,170)
        self.criteria_3.adjustSize() 
        
        self.typiki_apodosi=QLineEdit(content)
        self.typiki_apodosi.setAlignment(Qt.AlignCenter)
        self.typiki_apodosi.setValidator(self.validator)       
        self.typiki_apodosi.move(600,170)
        self.typiki_apodosi.textChanged.connect(self.critiria_moria_3)
        self.typiki_apodosi.textChanged.connect(self.biolog_pososto)
        self.typiki_apodosi.textChanged.connect(self.epilex_ta)
        
        self.moria_3=QLineEdit(content)
        self.moria_3.setAlignment(Qt.AlignCenter)
        self.moria_3.setReadOnly(True) 
        self.moria_3.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')        
        self.moria_3.move(860,170)
        self.moria_3.textChanged.connect(self.sum_total_moria)
        
        self.criteria_4=QLabel(content)
        self.criteria_4.setText('4. Ετήσιος Κύκλος εργασιών (μέσος όρος τριετίας)')
        self.criteria_4.move(10,230)
        self.criteria_4.adjustSize() 
        
        self.kyklos_2021=QLineEdit(content)
        self.kyklos_2021.setAlignment(Qt.AlignCenter)         
        self.kyklos_2021.move(600,220)
        self.kyklos_2021.textChanged.connect(self.mean_trietias)
        self.kyklos_2021.setValidator(self.validator)
        
        self.kyklos_2021_title=QLabel(content)
        self.kyklos_2021_title.setText("2021")
        self.kyklos_2021_title.move(600,200)
        
        self.kyklos_2022=QLineEdit(content)
        self.kyklos_2022.setAlignment(Qt.AlignCenter)         
        self.kyklos_2022.move(600,270)
        self.kyklos_2022.textChanged.connect(self.mean_trietias)
        self.kyklos_2022.setValidator(self.validator)
        
        self.kyklos_2022_title=QLabel(content)
        self.kyklos_2022_title.setText("2022")
        self.kyklos_2022_title.move(600,250)
        
        self.kyklos_2023=QLineEdit(content)
        self.kyklos_2023.setAlignment(Qt.AlignCenter)         
        self.kyklos_2023.move(600,320)
        self.kyklos_2023.textChanged.connect(self.mean_trietias)
        self.kyklos_2023.setValidator(self.validator)
        
        self.kyklos_2023_title=QLabel(content)
        self.kyklos_2023_title.setText("2023")
        self.kyklos_2023_title.move(600,300)
        
        self.mean_trietias_apotel=QLineEdit(content)
        self.mean_trietias_apotel.setAlignment(Qt.AlignCenter)
        self.mean_trietias_apotel.setReadOnly(True) 
        self.mean_trietias_apotel.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.mean_trietias_apotel.textChanged.connect(self.critiria_moria_4)
        self.mean_trietias_apotel.move(730,270)
        
        self.moria_4=QLineEdit(content)
        self.moria_4.setAlignment(Qt.AlignCenter)
        self.moria_4.setReadOnly(True)  
        self.moria_4.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.moria_4.move(860,270)
        self.moria_4.textChanged.connect(self.sum_total_moria)
        
        self.criteria_5=QLabel(content)
        self.criteria_5.setText('5. Πιστοποιημένη βιολογική παραγωγή σε ποσοστό >50% της συνολικής Τ.Α. κατά την αρχική κατάσταση.')
        self.criteria_5.move(10,370)
        self.criteria_5.adjustSize() 
        
        self.biologica=QLineEdit(content)
        self.biologica.setAlignment(Qt.AlignCenter)         
        self.biologica.move(600,360)
        self.biologica.setValidator(self.validator)
        self.biologica.textChanged.connect(self.biolog_pososto)
        
        self.biologica_pososto=QLineEdit(content)
        self.biologica_pososto.setAlignment(Qt.AlignCenter)         
        self.biologica_pososto.move(730,360)
        self.biologica_pososto.setReadOnly(True)  
        self.biologica_pososto.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.biologica_pososto.textChanged.connect(self.critiria_moria_5)
        
        self.moria_5=QLineEdit(content)
        self.moria_5.setAlignment(Qt.AlignCenter)
        self.moria_5.setReadOnly(True)  
        self.moria_5.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.moria_5.move(860,360)
        self.moria_5.textChanged.connect(self.sum_total_moria)
        
        self.criteria_6_a=QLabel(content)
        self.criteria_6_a.setText('6α.Τεκμηριωμένη ικανότητα κάλυψης του αιτούμενου προϋπολογισμού κατά την υποβολή της αίτησης στήριξης.')
        self.criteria_6_a.move(10,420)
        self.criteria_6_a.adjustSize() 
        
        self.idia_simmetoxi=QLineEdit(content)
        self.idia_simmetoxi.setAlignment(Qt.AlignCenter)
        self.idia_simmetoxi.setValidator(self.validator)    
        self.idia_simmetoxi.move(600,410)
        self.idia_simmetoxi.textChanged.connect(self.simmetoxi_pososto)
        self.idia_simmetoxi.textChanged.connect(self.critiria_moria_6_a)
        
        self.idia_simmetoxi_pososto=QLineEdit(content)
        self.idia_simmetoxi_pososto.setAlignment(Qt.AlignCenter)
        self.idia_simmetoxi_pososto.setValidator(self.validator)   
        self.idia_simmetoxi_pososto.setReadOnly(True)
        self.idia_simmetoxi_pososto.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.idia_simmetoxi_pososto.move(730,410)
        
        self.moria_6_a=QLineEdit(content)
        self.moria_6_a.setAlignment(Qt.AlignCenter)
        self.moria_6_a.setReadOnly(True)  
        self.moria_6_a.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.moria_6_a.move(860,410)
        self.moria_6_a.textChanged.connect(self.sum_total_moria)
        
        self.criteria_6_b=QLabel(content)
        self.criteria_6_b.setText('6.β Ύπαρξη φορολογικής ενημερότητας τουλάχιστον δίμηνης διάρκειας και ασφαλιστικές ενημερότητες\n τουλάχιστον εξάμηνης διάρκειας')
        self.criteria_6_b.move(10,480)
        self.criteria_6_b.adjustSize() 
        
        self.combo_6_b = NoWheelComboBox(content)
        self.combo_6_b.addItems(["Επιλέξτε","Ναι", "Όχι"])
        self.combo_6_b.move(600,480)
        self.combo_6_b.currentIndexChanged.connect(self.critiria_moria_6_b)
        self.combo_6_b.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        
        self.moria_6_b=QLineEdit(content)
        self.moria_6_b.setAlignment(Qt.AlignCenter)
        self.moria_6_b.setReadOnly(True) 
        self.moria_6_b.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.moria_6_b.move(860,480)
        self.moria_6_b.textChanged.connect(self.sum_total_moria)
        
        self.criteria_6_c=QLabel(content)
        self.criteria_6_c.setText('6.γ Ύπαρξη κερδοφορίας κατά τις 3 τελευταίες διαχειριστικές χρήσεις (μέσος όρος 3ετίας/διαθέσιμων ετών)\nπρο αποσβέσεων και φόρων')
        self.criteria_6_c.move(10,540)
        self.criteria_6_c.adjustSize() 
        
        self.apotelesmata_2021=QLineEdit(content)
        self.apotelesmata_2021.setAlignment(Qt.AlignCenter)         
        self.apotelesmata_2021.move(600,530)
        self.apotelesmata_2021.textChanged.connect(self.mean_diathesima)
        self.apotelesmata_2021.setValidator(self.validator)
        
        self.apotelesmata_2021_title=QLabel(content)
        self.apotelesmata_2021_title.setText("2021")
        self.apotelesmata_2021_title.move(600,510)
        
        self.apotelesmata_2022=QLineEdit(content)
        self.apotelesmata_2022.setAlignment(Qt.AlignCenter)         
        self.apotelesmata_2022.move(600,580)
        self.apotelesmata_2022.textChanged.connect(self.mean_diathesima)
        self.apotelesmata_2022.setValidator(self.validator)
        
        self.apotelesmata_2022_title=QLabel(content)
        self.apotelesmata_2022_title.setText("2022")
        self.apotelesmata_2022_title.move(600,560)
        
        self.apotelesmata_2023=QLineEdit(content)
        self.apotelesmata_2023.setAlignment(Qt.AlignCenter)         
        self.apotelesmata_2023.move(600,630)
        self.apotelesmata_2023.textChanged.connect(self.mean_diathesima)
        self.apotelesmata_2023.setValidator(self.validator)
        
        self.apotelesmata_2023_title=QLabel(content)
        self.apotelesmata_2023_title.setText("2023")
        self.apotelesmata_2023_title.move(600,610)
        
        self.mean_apotel=QLineEdit(content)
        self.mean_apotel.setAlignment(Qt.AlignCenter)
        self.mean_apotel.setReadOnly(True) 
        self.mean_apotel.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.mean_apotel.textChanged.connect(self.critiria_moria_6_c)
        self.mean_apotel.move(730,580)        
           
                  
        self.moria_6_c=QLineEdit(content)
        self.moria_6_c.setAlignment(Qt.AlignCenter)
        self.moria_6_c.setReadOnly(True) 
        self.moria_6_c.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_6_c.move(860,580)
        self.moria_6_c.textChanged.connect(self.sum_total_moria)
        
        self.criteria_7=QLabel(content)
        self.criteria_7.setText('7. Ο υποψήφιος είναι Ν. Αγρόττης του 2021 ή της Παρέμβασης Π3-75.1 ή φυσικό πρόσωπο με\n εμπειρία άνω των 5 ετών και ηλικία έως και 50 ετών')
        self.criteria_7.move(10,690)
        self.criteria_7.adjustSize() 
        
        self.combo_7 = NoWheelComboBox(content)
        self.combo_7.addItems(["Επιλέξτε","Ν.Αγρότης 2021", "Ν.Αγρότης Π3-75.1", "Εμπειρία>5ετών και ηλικία<=50 ετών", "Όχι"])
        self.combo_7.move(600,690)
        self.combo_7.currentIndexChanged.connect(self.critiria_moria_7)
        self.combo_7.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        
        self.moria_7=QLineEdit(content)
        self.moria_7.setAlignment(Qt.AlignCenter)
        self.moria_7.setReadOnly(True) 
        self.moria_7.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_7.move(860,690)
        self.moria_7.textChanged.connect(self.sum_total_moria)
        
        self.criteria_8=QLabel(content)
        self.criteria_8.setText('8. Επιλέξτε το επίπεδο εκπαίδευσης στο Εθνικό Πλαίσιο Προσόντων του υποψηφίου')
        self.criteria_8.move(10,760)
        self.criteria_8.adjustSize() 
        
        self.combo_8 = NoWheelComboBox(content)
        self.combo_8.addItems(["Επιλέξτε","6,7 ή 8", "Γεωτεχνικός 3,4 ή 5", "Γεωτεχνικός 6,7 ή 8", "Κανένα από τα παραπάνω"])
        self.combo_8.move(600,760)
        self.combo_8.currentIndexChanged.connect(self.critiria_moria_8)
        self.combo_8.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        
        self.moria_8=QLineEdit(content)
        self.moria_8.setAlignment(Qt.AlignCenter)
        self.moria_8.setReadOnly(True) 
        self.moria_8.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_8.move(860,760)
        self.moria_8.textChanged.connect(self.sum_total_moria)
        
        self.criteria_9=QLabel(content)
        self.criteria_9.setText('9. Επιλέξτε εάν ο υποψήφιος είναι μέλος σε συλλογικά σχήματα')
        self.criteria_9.move(10,820)
        self.criteria_9.adjustSize() 
        
        self.combo_9 = NoWheelComboBox(content)
        self.combo_9.addItems(["Επιλέξτε","ΟμΠ/ΟΠ", "ΑΣ", "ΑΣ και ΟμΠ/ΟΠ", "Αναγκαστικός συνεταιρισμός", "Κανένα από τα παραπάνω"])
        self.combo_9.move(600,820)
        self.combo_9.currentIndexChanged.connect(self.critiria_moria_9)
        self.combo_9.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        
        self.moria_9=QLineEdit(content)
        self.moria_9.setAlignment(Qt.AlignCenter)
        self.moria_9.setReadOnly(True) 
        self.moria_9.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_9.move(860,820)
        self.moria_9.textChanged.connect(self.sum_total_moria)
        
        self.criteria_10=QLabel(content)
        self.criteria_10.setText('10. Συμπληρώστε το ποσό των δαπανών που αφορούν σε ανέγερση ή επέκταση θερμοκηπιακών εγκαταστάσεων')
        self.criteria_10.move(10,880)
        self.criteria_10.adjustSize() 
        
        self.poso_ktiriaka=QLineEdit(content)
        self.poso_ktiriaka.setAlignment(Qt.AlignCenter)         
        self.poso_ktiriaka.move(600,880)
        self.poso_ktiriaka.textChanged.connect(self.poso_ktiriaka_pososto)
        self.poso_ktiriaka.textChanged.connect(self.critiria_moria_10)
        self.poso_ktiriaka.setValidator(self.validator)
        
        self.ktiriaka_pososto=QLineEdit(content)
        self.ktiriaka_pososto.setAlignment(Qt.AlignCenter)
        self.ktiriaka_pososto.setValidator(self.validator)   
        self.ktiriaka_pososto.setReadOnly(True)
        self.ktiriaka_pososto.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.ktiriaka_pososto.move(730,880)
        
        self.moria_10=QLineEdit(content)
        self.moria_10.setAlignment(Qt.AlignCenter)
        self.moria_10.setReadOnly(True) 
        self.moria_10.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_10.move(860,880)
        self.moria_10.textChanged.connect(self.sum_total_moria)
        
        self.criteria_11=QLabel(content)
        self.criteria_11.setText('11. Συμπληρώστε το ποσό των δαπανών που αφορούν σε εκσυγχρονισμό θερμοκηπιακών εγκαταστάσεων')
        self.criteria_11.move(10,940)
        self.criteria_11.adjustSize() 
        
        self.poso_eksixronismou=QLineEdit(content)
        self.poso_eksixronismou.setAlignment(Qt.AlignCenter)         
        self.poso_eksixronismou.move(600,940)
        self.poso_eksixronismou.textChanged.connect(self.poso_eksixronismos_pososto)
        self.poso_eksixronismou.textChanged.connect(self.critiria_moria_11)
        self.poso_eksixronismou.setValidator(self.validator)
        
        self.eksixronismos_pososto=QLineEdit(content)
        self.eksixronismos_pososto.setAlignment(Qt.AlignCenter)
        self.eksixronismos_pososto.setValidator(self.validator)   
        self.eksixronismos_pososto.setReadOnly(True)
        self.eksixronismos_pososto.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.eksixronismos_pososto.move(730,940)
        
        self.moria_11=QLineEdit(content)
        self.moria_11.setAlignment(Qt.AlignCenter)
        self.moria_11.setReadOnly(True) 
        self.moria_11.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_11.move(860,940)
        self.moria_11.textChanged.connect(self.sum_total_moria)
        
        self.criteria_12=QLabel(content)
        self.criteria_12.setText('12. Συμπληρώστε το ποσό των δαπανών που αφορούν σε ΑΠΕ')
        self.criteria_12.move(10,1000)
        self.criteria_12.adjustSize() 
        
        self.poso_ape=QLineEdit(content)
        self.poso_ape.setAlignment(Qt.AlignCenter)         
        self.poso_ape.move(600,1000)
        self.poso_ape.textChanged.connect(self.poso_ape_pososto)
        self.poso_ape.textChanged.connect(self.critiria_moria_12)
        self.poso_ape.setValidator(self.validator)
        
        self.ape_pososto=QLineEdit(content)
        self.ape_pososto.setAlignment(Qt.AlignCenter)
        self.ape_pososto.setValidator(self.validator)   
        self.ape_pososto.setReadOnly(True)
        self.ape_pososto.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.ape_pososto.move(730,1000)
        
        self.moria_12=QLineEdit(content)
        self.moria_12.setAlignment(Qt.AlignCenter)
        self.moria_12.setReadOnly(True) 
        self.moria_12.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_12.move(860,1000)
        self.moria_12.textChanged.connect(self.sum_total_moria)
        
        self.criteria_13=QLabel(content)
        self.criteria_13.setText('13. H έδρα του υποψήφιου βρίσκεται σε ηπειρωτικές περιοχές που συμπεριλαμβάνονται στα Εδαφικά Σχέδια\n Δίκαιης Μετάβασης (ΕΣΔΙΜ).')
        self.criteria_13.move(10,1060)
        self.criteria_13.adjustSize() 
        
        self.combo_13 = NoWheelComboBox(content)
        self.combo_13.addItems(["Επιλέξτε","Ναι", "Όχι"])
        self.combo_13.move(600,1060)
        self.combo_13.currentIndexChanged.connect(self.critiria_moria_13)
        self.combo_13.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        
        self.moria_13=QLineEdit(content)
        self.moria_13.setAlignment(Qt.AlignCenter)
        self.moria_13.setReadOnly(True) 
        self.moria_13.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0; color:}')
        self.moria_13.move(860,1060)
        self.moria_13.textChanged.connect(self.sum_total_moria)
        
        
        #κουμπί καθαρισμού και αθροίσματος
        self.button_clear=QPushButton(content, text="Καθαρισμός")
        self.button_clear.move(890,1140)
        self.button_clear.clicked.connect(self.clear_data)
        
        self.total_moria=QLineEdit(content)
        self.total_moria.setAlignment(Qt.AlignCenter)
        self.total_moria.setReadOnly(True)      
        self.total_moria.move(860,1100)
        self.total_moria.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        self.total_moria.textChanged.connect(self.epilex_moria)
        
        self.total_moria_title=QLabel(content)
        self.total_moria_title.setText("Σύνολο βαθμολογίας")
        self.total_moria_title.move(750,1100)
        
        self.export_xls = QPushButton("Εξαγωγή σε Excel", content)
        self.export_xls.move(990, 1140)
        self.export_xls.clicked.connect(self.export_to_excel)
        
        #Ένδειξη επιλεξιμότητας
        self.epileximo_budget=QLineEdit(content)
        self.epileximo_budget.setAlignment(Qt.AlignCenter)
        self.epileximo_budget.setReadOnly(True)      
        self.epileximo_budget.move(1000,0)
        self.epileximo_budget.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        
        self.epileximi_ta=QLineEdit(content)
        self.epileximi_ta.setAlignment(Qt.AlignCenter)
        self.epileximi_ta.setReadOnly(True)      
        self.epileximi_ta.move(1000,170)
        self.epileximi_ta.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        
        self.epilexima_moria=QLineEdit(content)
        self.epilexima_moria.setAlignment(Qt.AlignCenter)
        self.epilexima_moria.setReadOnly(True)      
        self.epilexima_moria.move(1000,1100)
        self.epilexima_moria.setStyleSheet('QLineEdit[readOnly=true]{background-color: #e0e0e0;}')
        
        scroll.setWidget(content)
        self.setCentralWidget(scroll)  
        
        
    # Συναρτήσεις με τις οποίες υπολογίστηκαν τα ποσοστά και η μοριοδότηση κάθε κριτηρίου   
        
    def critiria_moria_1(self):
        
        if self.combo_1.currentText()=="Ναι":
            self.moria_1.setText("10")
        elif self.combo_1.currentText()=="Όχι":
            self.moria_1.setText("0")
        else:
            self.moria_1.setText("")        
            
        
            
    def critiria_moria_2(self):
        try:
            a_text=self.esoda_agro.text().strip()
            b_text=self.esoda.text().strip()
            if a_text and b_text:                
                a=float(a_text)
                b=float(b_text)
            
                if b!=0 and a/b>0.7 and a/b<=1:
                    self.moria_2.setText("4")
                                
                else:
                    self.moria_2.setText("0")
            else:
                self.moria_2.setText("0")
            
        except (ValueError, TypeError):
            self.moria_2.setText("0")
            
            
    def esoda_pososto(self):
        try:
            a_text=self.esoda_agro.text().strip()
            b_text=self.esoda.text().strip()
            
            if a_text and b_text:               
              
                a=float(a_text)
                b=float(b_text)
                
                if b!=0:
                    total=(a/b)*100
                    total_round=round(total,2)
                    str_total=str(total_round)+"%"
                    self.esoda_pososto.setText(str_total)
                else: self.esoda_pososto.setText("0")
            
            else:
                self.esoda_pososto.setText("0")
                    
        except (ValueError, TypeError):
            self.esoda_pososto.setText("0")
            
    
    def critiria_moria_3(self):
        try:
            a_text=self.typiki_apodosi.text().strip()
            if a_text:
        
                if float(a_text)<20000:
                    self.moria_3.setText("2.5")
                elif float(a_text)>=20000 and float(a_text)<=40000:
                    input_ta=float(self.typiki_apodosi.text())
                    moria=np.interp(input_ta, [20000, 40000], [50, 100])
                    final_moria=(moria*0.05)
                    final_moria_round=round(final_moria,2)
                    final_moria_round_str=str(final_moria_round)
                    self.moria_3.setText(final_moria_round_str)
                elif float(a_text)>40000:
                    self.moria_3.setText("5")
                else:
                    self.moria_3.setText("0")
            else:
                self.moria_3.setText("0")
        except (ValueError, TypeError):
            self.moria_3.setText("0")
            
           
            
    def mean_trietias(self):                      
        try:
            texts=[
            self.kyklos_2021.text().strip(),
            self.kyklos_2022.text().strip(),
            self.kyklos_2023.text().strip()
            ]
            values=[]
            for i in texts:
                if i:
                    val= float(i)
                    if val>=0:
                        values.append(float(val))
            if values :
                mean_value=round(sum(values)/len(values),2) 
                mean_value_str=str(mean_value)
            
                self.mean_trietias_apotel.setText(mean_value_str)                  
           
            else:
                self.mean_trietias_apotel.setText("0")
                
                
        except (ValueError, TypeError):
            self.mean_trietias_apotel.setText("0")
                
                
        except (ValueError, TypeError):
            self.mmean_trietias_apotel.setText("0")
        
    def critiria_moria_4(self):
        try:
            a_text=self.mean_trietias_apotel.text().strip()
            if a_text:
              a=float(a_text)
              if a<=500000 and a>0:
                  self.moria_4.setText("5.4")
              elif a>500000 and a<=1000000:
                  self.moria_4.setText("6.75")
              elif a>1000000:
                  self.moria_4.setText("9")
              else:
                  self.moria_4.setText("0")
            else:
                self.moria_4.setText("0")
        except (ValueError, TypeError):
            self.moria_4.setText("0")
            
          
    def biolog_pososto(self):
        try:            
            a_text=self.biologica.text()
            b_text=self.typiki_apodosi.text().strip()
            if a_text and b_text:                
                a=float(a_text)
                b=float(b_text)
                
                if b!=0:                
                    pososto=a/b*100
                    pososto_round=round(pososto,2)
                    pososto_str=str(pososto_round)+"%"
                    self.biologica_pososto.setText(pososto_str)
                else:
                    self.biologica_pososto.setText("0")
            else:
                self.biologica_pososto.setText("0")
        except (ValueError, TypeError):
            self.biologica_pososto.setText("0")
           
            
          
    def critiria_moria_5(self):
        try:            
            a_text=self.biologica.text().strip()
            b_text=self.typiki_apodosi.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                if b!=0:
                    c=a/b
                    c_round=round(c,2)
                    if c_round>0.5 and c_round<=1:
                        self.moria_5.setText("2")
                    else:
                        self.moria_5.setText("0")
                else:
                    self.moria_5.setText("0")
            else:
                self.moria_5.setText("0")
        except (ValueError, TypeError):
            self.moria_5.setText("0")
            
    def simmetoxi_pososto(self):
        try:
            a_text=self.idia_simmetoxi.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                
                if b!=0:
                    pososto_idia=a/b*100
                    pososto_idia_round=round(pososto_idia,2)
                    pososto_idia_str=str(pososto_idia_round)+"%"
                    self.idia_simmetoxi_pososto.setText(pososto_idia_str)
                else:
                    self.idia_simmetoxi_pososto.setText("0")
            else:
                self.idia_simmetoxi_pososto.setText("0")
        except (ValueError, TypeError):
            self.idia_simmetoxi_pososto.setText("0")
            
        
    def critiria_moria_6_a(self):
        try:
            a_text=self.idia_simmetoxi.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                if b!=0:
                    c_round=a/b
                    
                    if c_round<=0.2 or c_round>1:
                        self.moria_6_a.setText("0")
                        
                    elif c_round>0.5:
                        self.moria_6_a.setText("10")
                        
                    else:
                        moria=np.interp(c_round, [0.2, 0.5], [30, 50])
                        final_moria=(moria*0.2)
                        final_moria_round=round(final_moria,2)
                        final_moria_round_str=str(final_moria_round)
                        self.moria_6_a.setText(final_moria_round_str)
                           
                   
                else:
                    self.moria_6_a.setText("0")
            else:
                self.moria_6_a.setText("0")
        except (ValueError, TypeError):
            self.moria_6_a.setText("0")
            
    def critiria_moria_6_b(self):
        
        if self.combo_6_b.currentText()=="Ναι":
            self.moria_6_b.setText("8")
        elif self.combo_6_b.currentText()=="Όχι":
            self.moria_6_b.setText("0")
        else:
            self.moria_6_b.setText("")   
            
    def mean_diathesima(self):
          try:
              texts=[
              self.apotelesmata_2021.text().strip(),
              self.apotelesmata_2022.text().strip(),
              self.apotelesmata_2023.text().strip()
              ]
              values=[]
              for i in texts:
                  if i:
                      val= float(i)
                      values.append(float(val))
              if values :
                  mean_value=round(sum(values)/len(values),2) 
                  mean_value_str=str(mean_value)
              
                  self.mean_apotel.setText(mean_value_str)                  
             
              else:
                  self.mean_apotel.setText("0")
                  
                  
          except (ValueError, TypeError):
              self.mean_apotel.setText("0")
              
        
    def critiria_moria_6_c(self):
        try:
        
            a_text=float(self.mean_apotel.text())
            if a_text>0:                
            
                self.moria_6_c.setText("2")            
                
            else:
                self.moria_6_c.setText("0")
                
        except (ValueError, TypeError):
            self.moria_6_c.setText("0")
            
    
    def critiria_moria_7(self):
        
        if self.combo_7.currentText()=="Ν.Αγρότης 2021" or self.combo_7.currentText()=="Ν.Αγρότης Π3-75.1" or self.combo_7.currentText()=="Εμπειρία>5ετών και ηλικία<=50 ετών":
            self.moria_7.setText("5")
        elif self.combo_7.currentText()=="Όχι":
            self.moria_7.setText("0")
        
        else:
            self.moria_7.setText("")  
    
    def critiria_moria_8(self):
        if self.combo_8.currentText()=="6,7 ή 8":
            self.moria_8.setText("3.5")
        elif self.combo_8.currentText()=="Γεωτεχνικός 3,4 ή 5":
            self.moria_8.setText("3.5")
        elif self.combo_8.currentText()=="Γεωτεχνικός 6,7 ή 8":
            self.moria_8.setText("5")
        elif self.combo_8.currentText()=="Κανένα από τα παραπάνω":
                self.moria_8.setText("0")
        else:
            self.moria_8.setText("")
            
    def critiria_moria_9(self):
        if self.combo_9.currentText()=="ΟμΠ/ΟΠ":
            self.moria_9.setText("2")
        elif self.combo_9.currentText()=="ΑΣ και ΟμΠ/ΟΠ":
            self.moria_9.setText("5")
        elif self.combo_9.currentText()=="Αναγκαστικός συνεταιρισμός":
            self.moria_9.setText("5")            
        elif self.combo_9.currentText()=="ΑΣ":
            self.moria_9.setText("3")            
        elif self.combo_9.currentText()=="Κανένα από τα παραπάνω":
                self.moria_9.setText("0")
        else:
            self.moria_9.setText("")
    
    def poso_ktiriaka_pososto(self):
        try:
            a_text=self.poso_ktiriaka.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                
                if b!=0:
                    pososto=a/b*100
                    pososto_round=round(pososto,2)
                    pososto_str=str(pososto_round)+"%"
                    self.ktiriaka_pososto.setText(pososto_str)
                else:
                    self.ktiriaka_pososto.setText("0")
            else:
                self.ktiriaka_pososto.setText("0")
        except (ValueError, TypeError):
            self.ktiriaka_pososto.setText("0")

    def critiria_moria_10(self):
        try:
            a_text=self.poso_ktiriaka.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                if b!=0:
                    c_round=a/b
                    
                    if c_round<=0.2 or c_round>1:
                        self.moria_10.setText("0")
                        
                    elif c_round>0.4 :
                        self.moria_10.setText("20")
                    else: 
                        moria=np.interp(c_round, [0.20, 0.40], [50, 100])
                        final_moria=(moria*0.2)
                        final_moria_round=round(final_moria,2)
                        final_moria_round_str=str(final_moria_round)
                        self.moria_10.setText(final_moria_round_str)
                         
                else:
                    self.moria_10.setText("0")
            else:
                self.moria_10.setText("0")
        except (ValueError, TypeError):
            self.moria_10.setText("0")   
    
    def poso_eksixronismos_pososto(self):
        try:
            a_text=self.poso_eksixronismou.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                
                if b!=0:
                    pososto=a/b*100
                    pososto_round=round(pososto,2)
                    pososto_str=str(pososto_round)+"%"
                    self.eksixronismos_pososto.setText(pososto_str)
                else:
                    self.eksixronismos_pososto.setText("0")
            else:
                self.eksixronismos_pososto.setText("0")
        except (ValueError, TypeError):
            self.eksixronismos_pososto.setText("0")

    
    def critiria_moria_11(self):
        try:
            a_text=self.poso_eksixronismou.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                if b!=0:
                    c_round=a/b
                    
                    if c_round<=0.2 or c_round>1:
                        self.moria_11.setText("0")
                        
                    elif c_round>0.4 :
                        self.moria_11.setText("9")
                    else: 
                        moria=np.interp(c_round, [0.20, 0.40], [50, 100])
                        final_moria=(moria*0.09)
                        final_moria_round=round(final_moria,2)
                        final_moria_round_str=str(final_moria_round)
                        self.moria_11.setText(final_moria_round_str)
                         
                else:
                    self.moria_11.setText("0")
            else:
                self.moria_11.setText("0")
        except (ValueError, TypeError):
            self.moria_11.setText("0")      
    
    def poso_ape_pososto(self):
        try:
            a_text=self.poso_ape.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                
                if b!=0:
                    pososto=a/b*100
                    pososto_round=round(pososto,2)
                    pososto_str=str(pososto_round)+"%"
                    self.ape_pososto.setText(pososto_str)
                else:
                    self.ape_pososto.setText("0")
            else:
                self.ape_pososto.setText("0")
        except (ValueError, TypeError):
            self.eksixronismos_pososto.setText("0")

    
    def critiria_moria_12(self):
        try:
            a_text=self.poso_ape.text().strip()
            b_text=self.input_budget.text().strip()
            if a_text and b_text:
                a=float(a_text)
                b=float(b_text)
                if b!=0:
                    c_round=a/b
                    
                    if c_round< 0.3 or c_round>1:
                        self.moria_12.setText("0")
                    
                    else:
                        self.moria_12.setText("6")                        
                                             
                else:
                    self.moria_12.setText("0")
            else:
                self.moria_12.setText("0")
        except (ValueError, TypeError):
            self.moria_12.setText("0")   
            
    def critiria_moria_13(self):
        if self.combo_13.currentText()=="Ναι":
            self.moria_13.setText("4")
        elif self.combo_13.currentText()=="Όχι":
            self.moria_13.setText("0")
        else:
            self.moria_13.setText("")
            
  #Συναρτήσεις καθαρισμού και αθροίσματος
    
    def clear_data(self):
        self.input_budget.clear()
        self.moria_1.clear()
        self.combo_1.setCurrentIndex(0)
        self.esoda_agro.clear()
        self.esoda.clear()
        self.esoda_pososto.clear()
        self.moria_2.clear()
        self.typiki_apodosi.clear()
        self.moria_3.clear()
        self.kyklos_2021.clear()
        self.kyklos_2022.clear()
        self.kyklos_2023.clear()
        self.mean_trietias_apotel.clear()
        self.moria_4.clear()
        self.biologica.clear()
        self.biologica_pososto.clear()
        self.moria_5.clear()
        self.idia_simmetoxi.clear()
        self.idia_simmetoxi_pososto.clear()
        self.moria_6_a.clear()
        self.moria_6_b.clear()
        self.combo_6_b.setCurrentIndex(0)
        self.apotelesmata_2021.clear()
        self.apotelesmata_2022.clear()
        self.apotelesmata_2023.clear()
        self.mean_apotel.clear()
        self.moria_6_c.clear()
        self.total_moria.clear()
        self.combo_7.setCurrentIndex(0)
        self.moria_7.clear()
        self.combo_8.setCurrentIndex(0)
        self.moria_8.clear()
        self.combo_9.setCurrentIndex(0)
        self.moria_9.clear()
        self.poso_ktiriaka.clear()
        self.ktiriaka_pososto.clear()
        self.moria_10.clear()
        self.poso_eksixronismou.clear()
        self.eksixronismos_pososto.clear()
        self.moria_11.clear()
        self.poso_ape.clear()
        self.ape_pososto.clear()
        self.moria_12.clear()
        self.combo_13.setCurrentIndex(0)
        self.moria_13.clear()
        self.onoma.clear()
        
        if self.total_moria.clear():
            self.total_moria.clear()
            
    
    
    def sum_total_moria(self):
        a_1=float(self.moria_1.text() or 0)
        a_2=float(self.moria_2.text() or 0)
        a_3=float(self.moria_3.text() or 0)
        a_4=float(self.moria_4.text() or 0)
        a_5=float(self.moria_5.text() or 0)
        a_6_1=float(self.moria_6_a.text() or 0)
        a_6_2=float(self.moria_6_b.text() or 0)
        a_6_3=float(self.moria_6_c.text() or 0)
        a_7=float(self.moria_7.text() or 0)
        a_8=float(self.moria_8.text() or 0)
        a_9=float(self.moria_9.text() or 0)
        a_10=float(self.moria_10.text() or 0)
        a_11=float(self.moria_11.text() or 0)
        a_12=float(self.moria_12.text() or 0)
        a_13=float(self.moria_13.text() or 0)
        total=sum([a_1, a_2, a_3, a_4, a_5, a_6_1, a_6_2, a_6_3, a_7, a_8, a_9, a_10, a_11, a_12, a_13])
        total_round=round(total,2)
        total_round_str=str(total_round)
        self.total_moria.setText(total_round_str)  
        
    #Συναρτήσεις ένδειξης επιλεξιμότητας 
    
    def epilex_budget(self):
        try:
            b_text=self.input_budget.text().strip()
            if  b_text:
                b=float(b_text)
                if b<30000 or b>1000000:
                    self.epileximo_budget.setText("ΜΗ ΕΠΙΛΕΞΙΜΟΣ")
                else :
                    self.epileximo_budget.setText("ΕΠΙΛΕΞΙΜΟΣ")
            else :
                self.epileximo_budget.setText("")
        except(ValueError,TypeError):
            self.epileximo_budget.setText("")
            
    def epilex_ta(self):
        try:
            b_text=self.typiki_apodosi.text().strip()
            if  b_text:
                b=float(b_text)
                if b<12000 :
                    self.epileximi_ta.setText("ΜΗ ΕΠΙΛΕΞΙΜΟΣ")
                else :
                    self.epileximi_ta.setText("ΕΠΙΛΕΞΙΜΟΣ")
            else :
                self.epileximi_ta.setText("")
        except(ValueError,TypeError):
            self.epileximi_ta.setText("")
            
            
    def epilex_moria(self):
        try:
            b_text=self.total_moria.text().strip()
            if  b_text:
                b=float(b_text)
                if b<30 :
                    self.epilexima_moria.setText("ΜΗ ΕΠΙΛΕΞΙΜΟΣ")
                else :
                    self.epilexima_moria.setText("ΕΠΙΛΕΞΙΜΟΣ")
            else :
                self.epilexima_moria.setText("")
        except(ValueError,TypeError):
            self.epilexima_moria.setText("")
            
    #Συνάρτηση για την εξαγωγή σε excel
            
    def export_to_excel(self):
        a_1=float(self.moria_1.text() or 0)
        a_2=float(self.moria_2.text() or 0)
        a_3=float(self.moria_3.text() or 0)
        a_4=float(self.moria_4.text() or 0)
        a_5=float(self.moria_5.text() or 0)
        a_6_1=float(self.moria_6_a.text() or 0)
        a_6_2=float(self.moria_6_b.text() or 0)
        a_6_3=float(self.moria_6_c.text() or 0)
        a_7=float(self.moria_7.text() or 0)
        a_8=float(self.moria_8.text() or 0)
        a_9=float(self.moria_9.text() or 0)
        a_10=float(self.moria_10.text() or 0)
        a_11=float(self.moria_11.text() or 0)
        a_12=float(self.moria_12.text() or 0)
        a_13=float(self.moria_13.text() or 0)
        a_total=float(self.total_moria.text() or 0)
        data={                 
             "Κριτήριο" :[
                 "Ονοματεπώνυμο :",
                "1. Kατοχή της ιδιότητας του επαγγελματία γεωργού", 
                "2. H προέλευση των ακαθάριστων εσόδων από την γεωργία είναι σημαντικά μεγαλύτερη από αυτή άλλων τομέων (>70%)",
                "3. Αξιολογείται και βαθμολογείται το οικονομικό μέγεθος της εκμετάλλευσης στην υφιστάμενη κατάσταση σε όρους \n τυπικής απόδοσης",
                "4. Ετήσιος Κύκλος εργασιών (μέσος όρος τριετίας)",
                "5. Πιστοποιημένη βιολογική παραγωγή σε ποσοστό >50% της συνολικής Τ.Α. κατά την αρχική κατάσταση.",
                "6α.Τεκμηριωμένη ικανότητα κάλυψης του αιτούμενου προϋπολογισμού κατά την υποβολή της αίτησης στήριξης.",
                "6.β Ύπαρξη φορολογικής ενημερότητας τουλάχιστον δίμηνης διάρκειας και ασφαλιστικές ενημερότητες\n τουλάχιστον εξάμηνης διάρκειας",
                "6.γ Ύπαρξη κερδοφορίας κατά τις 3 τελευταίες διαχειριστικές χρήσεις (μέσος όρος 3ετίας/διαθέσιμων ετών)\nπρο αποσβέσεων και φόρων",
                "7. Ο υποψήφιος είναι Ν. Αγρόττης του 2021 ή της Παρέμβασης Π3-75.1 ή φυσικό πρόσωπο με\n εμπειρία άνω των 5 ετών και ηλικία έως και 50 ετών",
                "8. Μοριοδοτείται το επίπεδο εκπαίδευσης στο Εθνικό Πλαίσιο Προσόντων του υποψηφίου",
                "9. Ο υποψήφιος είναι μέλος σε συλλογικά σχήματα",
                "10. Μοριοδοτούνται οι επενδύσεις ανέγερσης ή επέκτασης θερμοκηπιακών εγκαταστάσεων",
                "11. Μοριοδοτούνται οι επενδύσεις εκσυγχρονισμού θερμοκηπιακών εγκαταστάσεων",
                "12. Μοριοδοτούνται οι επενδύσεις σε ΑΠΕ",
                "13. H έδρα του υποψήφιου βρίσκεται σε ηπειρωτικές περιοχές που συμπεριλαμβάνονται στα Εδαφικά Σχέδια Δίκαιης Μετάβασης (ΕΣΔΙΜ)",
                "Συνολική βαθμολογία υποψηφίου : "                
                
                ],
            "Μόρια": [
                self.onoma.text(),
                a_1,
                a_2,
                a_3,
                a_4,
                a_5,
                a_6_1,
                a_6_2,
                a_6_3,
                a_7,
                a_8,
                a_9,
                a_10,
                a_11,
                a_12,
                a_13,
                a_total                
                ]
            }
        
        df=pd.DataFrame(data)
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self,
                                                "Αποθήκευση Excel",
                                                "Μοριοδοτηση.xlsx",
                                                "Excel Files (*.xlsx);;All Files (*)",
                                                options=options)
        if not filename:
            return
        
        if not filename.lower().endswith(".xlsx"):
            filename+=".xlsx"
           
        try:
            
            df.to_excel(filename, index=False)
            
        except Exception as e:
            QMessageBox.critical(self, "Σφάλμα", f"Αδυναμία αποθήκευσης αρχείου:\n{e}")
        
app = QtWidgets.QApplication(sys.argv)
window=MainWindow()

window.show()

sys.exit(app.exec_())