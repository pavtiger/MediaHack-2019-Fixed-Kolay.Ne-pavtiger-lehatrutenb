#include "mainwindow.h"
#include <QApplication>
#include <QDesktopServices>
#include <QtWebEngineWidgets/qwebenginepage.h>
#include <QUrl>
#include <QtWebView>
#include <QDesktopServices>
#include <Windows.h>
#include <vector>
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
