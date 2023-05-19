# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc
import images_for_UI_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 782)
        MainWindow.setStyleSheet(u"*{ \n"
"border: none;\n"
"background-color: transparent;\n"
"background: none;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff\n"
"\n"
"}\n"
"#centralwidget{\n"
"background-color:  rgb(255, 0, 0)\n"
"}\n"
"\n"
"#leftMenuContainer{\n"
"background-color: #590004\n"
"}\n"
"\n"
"QPushButton{\n"
"text-align: left;\n"
"padding: 2px 5px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px\n"
"}\n"
"\n"
"#CenterMenuSubContainer{\n"
"background-color:#7A0006;\n"
"}\n"
"#frame_4{\n"
"background-color:#590004;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Menu_btn = QPushButton(self.frame)
        self.Menu_btn.setObjectName(u"Menu_btn")
        icon = QIcon()
        icon.addFile(u":/icons/project_icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_btn.setIcon(icon)
        self.Menu_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_3.addWidget(self.Menu_btn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Home_btn = QPushButton(self.frame_2)
        self.Home_btn.setObjectName(u"Home_btn")
        self.Home_btn.setStyleSheet(u"background-color: #7A0006")
        icon1 = QIcon()
        icon1.addFile(u":/icons/project_icons/home.svg", QSize(), QIcon.Normal, QIcon.On)
        self.Home_btn.setIcon(icon1)
        self.Home_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_4.addWidget(self.Home_btn)

        self.Models_btn = QPushButton(self.frame_2)
        self.Models_btn.setObjectName(u"Models_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/project_icons/layers.svg", QSize(), QIcon.Normal, QIcon.On)
        self.Models_btn.setIcon(icon2)
        self.Models_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_4.addWidget(self.Models_btn)

        self.Forecasting_btn = QPushButton(self.frame_2)
        self.Forecasting_btn.setObjectName(u"Forecasting_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/project_icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Forecasting_btn.setIcon(icon3)
        self.Forecasting_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_4.addWidget(self.Forecasting_btn)

        self.Datasets_btn = QPushButton(self.frame_2)
        self.Datasets_btn.setObjectName(u"Datasets_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/project_icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Datasets_btn.setIcon(icon4)
        self.Datasets_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_4.addWidget(self.Datasets_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Info_btn = QPushButton(self.frame_3)
        self.Info_btn.setObjectName(u"Info_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/project_icons/info.svg", QSize(), QIcon.Normal, QIcon.On)
        self.Info_btn.setIcon(icon5)
        self.Info_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_5.addWidget(self.Info_btn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.CenterMenuSubContainer = QWidget(self.centerMenuContainer)
        self.CenterMenuSubContainer.setObjectName(u"CenterMenuSubContainer")
        self.CenterMenuSubContainer.setStyleSheet(u"background-color:rgb(122, 0, 6)")
        self.verticalLayout_7 = QVBoxLayout(self.CenterMenuSubContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.CenterMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/project_icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(34, 34))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.CenterMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setStyleSheet(u"#label_3{\n"
"text-size:100px\n"
"}\n"
"\n"
"")
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.Home_page.setStyleSheet(u"background-color: #7A0006")
        self.verticalLayout_15 = QVBoxLayout(self.Home_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_11 = QFrame(self.Home_page)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_11)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_21 = QFrame(self.frame_11)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_21)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_11 = QLabel(self.frame_21)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size:21px")

        self.verticalLayout_27.addWidget(self.label_11)


        self.verticalLayout_26.addWidget(self.frame_21, 0, Qt.AlignBottom)

        self.frame_18 = QFrame(self.frame_11)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 50, 71, 71))
        self.label_12.setPixmap(QPixmap(u":/images/Images/istockphoto-1210939712-612x612.jpg"))
        self.label_12.setScaledContents(True)
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(120, 60, 121, 61))

        self.verticalLayout_26.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_11)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(120, 40, 111, 61))
        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 40, 71, 71))
        self.label_19.setPixmap(QPixmap(u":/images/Images/istockphoto-1210939712-612x612.jpg"))
        self.label_19.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(120, 50, 111, 61))
        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 40, 71, 71))
        self.label_15.setPixmap(QPixmap(u":/images/Images/istockphoto-1210939712-612x612.jpg"))
        self.label_15.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.frame_20)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.Home_page)
        self.Models_page = QWidget()
        self.Models_page.setObjectName(u"Models_page")
        self.verticalLayout_12 = QVBoxLayout(self.Models_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_14 = QFrame(self.Models_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#label_3{\n"
"text-size:50px\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_14)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:24px")
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_3, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size:24px")

        self.verticalLayout_20.addWidget(self.label_4)


        self.verticalLayout_12.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.Models_page)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setStyleSheet(u"background-color:#7A0006;\n"
"color:rgb(0, 0, 0)")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ModelsTable = QTableWidget(self.frame_9)
        if (self.ModelsTable.columnCount() < 1):
            self.ModelsTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.ModelsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.ModelsTable.setObjectName(u"ModelsTable")
        self.ModelsTable.setStyleSheet(u"background-color:rgb(255, 255, 255)\n"
"")

        self.verticalLayout_18.addWidget(self.ModelsTable)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.frame_10 = QFrame(self.Models_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.GenerateModels_btn = QPushButton(self.frame_10)
        self.GenerateModels_btn.setObjectName(u"GenerateModels_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/project_icons/codepen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.GenerateModels_btn.setIcon(icon7)
        self.GenerateModels_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_13.addWidget(self.GenerateModels_btn)


        self.verticalLayout_12.addWidget(self.frame_10, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.Models_page)
        self.Datasets_page = QWidget()
        self.Datasets_page.setObjectName(u"Datasets_page")
        sizePolicy1.setHeightForWidth(self.Datasets_page.sizePolicy().hasHeightForWidth())
        self.Datasets_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.Datasets_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_12 = QFrame(self.Datasets_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size:24px")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size:24px")

        self.verticalLayout_22.addWidget(self.label_6)


        self.verticalLayout_10.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.Datasets_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color:#7A0006;\n"
"color:rgb(0, 0, 0)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.DatasetTable = QTableWidget(self.frame_13)
        if (self.DatasetTable.columnCount() < 1):
            self.DatasetTable.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.DatasetTable.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.DatasetTable.setObjectName(u"DatasetTable")
        self.DatasetTable.setStyleSheet(u"background-color:rgb(255, 255, 255)\n"
"")

        self.verticalLayout_21.addWidget(self.DatasetTable)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.dataframe = QFrame(self.Datasets_page)
        self.dataframe.setObjectName(u"dataframe")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dataframe.sizePolicy().hasHeightForWidth())
        self.dataframe.setSizePolicy(sizePolicy3)
        self.dataframe.setStyleSheet(u"background-color:#7A0006;\n"
"color:rgb(0, 0, 0)")
        self.dataframe.setFrameShape(QFrame.StyledPanel)
        self.dataframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.dataframe)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.dataframe, 0, Qt.AlignVCenter)

        self.generatedataframe = QFrame(self.Datasets_page)
        self.generatedataframe.setObjectName(u"generatedataframe")
        self.generatedataframe.setFrameShape(QFrame.StyledPanel)
        self.generatedataframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.generatedataframe)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.GenerateData_btn = QPushButton(self.generatedataframe)
        self.GenerateData_btn.setObjectName(u"GenerateData_btn")
        self.GenerateData_btn.setIcon(icon7)
        self.GenerateData_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_11.addWidget(self.GenerateData_btn)


        self.verticalLayout_10.addWidget(self.generatedataframe, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.Datasets_page)
        self.Forecasting_page = QWidget()
        self.Forecasting_page.setObjectName(u"Forecasting_page")
        self.verticalLayout_8 = QVBoxLayout(self.Forecasting_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.Forecasting_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-size:24px")
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size:24px")

        self.verticalLayout_23.addWidget(self.label_8)


        self.verticalLayout_8.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.Forecasting_page)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"background-color:#7A0006;\n"
"color:rgb(0, 0, 0)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ForecastTable = QTableWidget(self.frame_6)
        if (self.ForecastTable.columnCount() < 1):
            self.ForecastTable.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ForecastTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.ForecastTable.setObjectName(u"ForecastTable")
        self.ForecastTable.setStyleSheet(u"background-color:rgb(255, 255, 255)\n"
"")

        self.verticalLayout_16.addWidget(self.ForecastTable)


        self.verticalLayout_8.addWidget(self.frame_6, 0, Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.frame_5 = QFrame(self.Forecasting_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Generate_Forecast_btn = QPushButton(self.frame_5)
        self.Generate_Forecast_btn.setObjectName(u"Generate_Forecast_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/project_icons/codepen.svg", QSize(), QIcon.Active, QIcon.Off)
        self.Generate_Forecast_btn.setIcon(icon8)
        self.Generate_Forecast_btn.setIconSize(QSize(41, 41))

        self.verticalLayout_9.addWidget(self.Generate_Forecast_btn)


        self.verticalLayout_8.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.Forecasting_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.CenterMenuSubContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.verticalLayout_14 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.mainbodyWidget = QStackedWidget(self.mainBodyContainer)
        self.mainbodyWidget.setObjectName(u"mainbodyWidget")
        self.mainbodyWidget.setStyleSheet(u"#label_10{\n"
"text-size:50px\n"
"}")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.homepage.setStyleSheet(u"#label_10{\n"
"font-size:31px\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.homepage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_8 = QFrame(self.homepage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"#label_10{\n"
"text-size:50px\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_16)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_7 = QFrame(self.frame_16)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"#label_10{\n"
"text-size:41px\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 9, 131, 121))
        self.label_2.setPixmap(QPixmap(u":/images/Images/MSU-IIT Logo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(466, 10, 131, 121))
        self.label_9.setPixmap(QPixmap(u":/images/Images/Thesis Logo.jpg"))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 20, 301, 91))
        self.label_10.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.frame_7)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_17)


        self.verticalLayout_24.addWidget(self.frame_16)


        self.verticalLayout_19.addWidget(self.frame_8)

        self.mainbodyWidget.addWidget(self.homepage)
        self.modelsPage = QWidget()
        self.modelsPage.setObjectName(u"modelsPage")
        self.verticalLayout_28 = QVBoxLayout(self.modelsPage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_22 = QFrame(self.modelsPage)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(0, 0, 1797, 1129))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_23)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"#label_10{\n"
"text-size:41px\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_24)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(9, 9, 131, 121))
        self.label_16.setPixmap(QPixmap(u":/images/Images/MSU-IIT Logo.jpg"))
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.frame_24)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(466, 10, 131, 121))
        self.label_17.setPixmap(QPixmap(u":/images/Images/Thesis Logo.jpg"))
        self.label_17.setScaledContents(True)
        self.label_20 = QLabel(self.frame_24)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(150, 20, 301, 91))
        self.label_20.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"font-size:34px")
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29.addWidget(self.frame_25)


        self.verticalLayout_28.addWidget(self.frame_22)

        self.mainbodyWidget.addWidget(self.modelsPage)
        self.ForecastsPage = QWidget()
        self.ForecastsPage.setObjectName(u"ForecastsPage")
        self.verticalLayout_30 = QVBoxLayout(self.ForecastsPage)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_26 = QFrame(self.ForecastsPage)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(0, 0, 619, 708))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_27)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#label_10{\n"
"text-size:41px\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_28)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(9, 9, 131, 121))
        self.label_21.setPixmap(QPixmap(u":/images/Images/MSU-IIT Logo.jpg"))
        self.label_21.setScaledContents(True)
        self.label_22 = QLabel(self.frame_28)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(466, 10, 131, 121))
        self.label_22.setPixmap(QPixmap(u":/images/Images/Thesis Logo.jpg"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.frame_28)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(150, 20, 301, 91))
        self.label_23.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"font-size:34px")
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_31.addWidget(self.frame_29)


        self.verticalLayout_30.addWidget(self.frame_26)

        self.mainbodyWidget.addWidget(self.ForecastsPage)
        self.DatasetPage = QWidget()
        self.DatasetPage.setObjectName(u"DatasetPage")
        self.verticalLayout_32 = QVBoxLayout(self.DatasetPage)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_30 = QFrame(self.DatasetPage)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_30)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_31)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"#label_10{\n"
"text-size:41px\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_32)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(9, 9, 131, 121))
        self.label_24.setPixmap(QPixmap(u":/images/Images/MSU-IIT Logo.jpg"))
        self.label_24.setScaledContents(True)
        self.label_25 = QLabel(self.frame_32)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(466, 10, 131, 121))
        self.label_25.setPixmap(QPixmap(u":/images/Images/Thesis Logo.jpg"))
        self.label_25.setScaledContents(True)
        self.label_26 = QLabel(self.frame_32)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(150, 20, 301, 91))
        self.label_26.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"font-size:34px")
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.frame_32)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(130, 240, 256, 192))
        self.tableWidget.setStyleSheet(u"color:rgb(0, 0, 0)")

        self.verticalLayout_33.addWidget(self.frame_32)


        self.verticalLayout_34.addWidget(self.frame_31)


        self.verticalLayout_32.addWidget(self.frame_30)

        self.mainbodyWidget.addWidget(self.DatasetPage)

        self.verticalLayout_14.addWidget(self.mainbodyWidget)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.mainbodyWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.Menu_btn.setText("")
#if QT_CONFIG(tooltip)
        self.Home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Home", None))
#endif // QT_CONFIG(tooltip)
        self.Home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.Models_btn.setToolTip(QCoreApplication.translate("MainWindow", u"See Models", None))
#endif // QT_CONFIG(tooltip)
        self.Models_btn.setText(QCoreApplication.translate("MainWindow", u"Models", None))
#if QT_CONFIG(tooltip)
        self.Forecasting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"See forecasts", None))
#endif // QT_CONFIG(tooltip)
        self.Forecasting_btn.setText(QCoreApplication.translate("MainWindow", u"Forecasting", None))
#if QT_CONFIG(tooltip)
        self.Datasets_btn.setToolTip(QCoreApplication.translate("MainWindow", u"See datasets", None))
#endif // QT_CONFIG(tooltip)
        self.Datasets_btn.setText(QCoreApplication.translate("MainWindow", u"Datasets", None))
#if QT_CONFIG(tooltip)
        self.Info_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.Info_btn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Options", None))
        self.pushButton.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"{THESIS NAME} Authors:", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>INSERT MEMBER NAME </p><p>and INFO</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>INSERT MEMBER NAME </p><p>and INFO</p></body></html>", None))
        self.label_19.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>INSERT MEMBER NAME </p><p>and INFO</p></body></html>", None))
        self.label_15.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select \"Model\"", None))
        self.label_4.setText("")
        ___qtablewidgetitem = self.ModelsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Models", None));
        self.GenerateModels_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Models", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Select \"Region\" to", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Display Datasets", None))
        ___qtablewidgetitem1 = self.DatasetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Regions", None));
        self.GenerateData_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Dataset", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Select \"Regions\" to", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"display Forecasts", None))
        ___qtablewidgetitem2 = self.ForecastTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Regions", None));
        self.Generate_Forecast_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Forecasts", None))
        self.label_2.setText("")
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"THESIS TITLE HERE", None))
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Models result", None))
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Forecasting", None))
        self.label_24.setText("")
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"DATASET", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DATASET", None));
    # retranslateUi

