#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDesktopServices>
#include <QUrl>
#include <QApplication>
#include <QtWebView>
#include <QMessageBox>
#include "lentwindow.h"
#include <QWidget>
#include <vector>
#include <iostream>
#include <string.h>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    setWindowIcon(QIcon("C:/Users/Andrey/Desktop/untitled1/qticon.ico"));
    setWindowTitle( tr("Kogora Filter") );

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{

    QString tags = ui->lineEdit_2->text();

    vector<string> arr;
        string str = tags.toUtf8().constData() ;
        string delim(", ");
        size_t prev = 0;
        size_t next;
        size_t delta = delim.length();

        while ((next = str.find(delim, prev)) != string::npos) {
            //Отладка-start
            string tmp = str.substr(prev, next - prev);
            cout << tmp << endl;
            //Отладка-end
            arr.push_back(str.substr(prev, next - prev));
            prev = next + delta;
        }
        //Отладка-start
        string tmp = str.substr(prev);
        cout << tmp << endl;
        //Отладка-end
        arr.push_back(str.substr(prev));

    QString ids = ui->lineEdit_3->text();

    LentWindow *window = new LentWindow ;
    window->show();
}

