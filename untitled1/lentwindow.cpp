#include "lentwindow.h"
#include "ui_lentwindow.h"

LentWindow::LentWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::LentWindow)
{
    setFixedSize(1116,620);
    setWindowIcon(QIcon("C:/Users/Andrey/Desktop/untitled1/qticon.ico"));


    ui->setupUi(this);
    this->setWindowTitle(tr("Feed") );
    //Server request required

    QString url = "https://vk.com/wall-159146575_1189883";
    ui->preview->load(QUrl(url));
    ui->preview->show();

    ui->textBrowser->setFixedSize(1096,620);
    ui->preview->setFixedSize(1076,600);

}

LentWindow::~LentWindow()
{
    delete ui;
}
