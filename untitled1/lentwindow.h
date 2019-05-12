#ifndef LENTWINDOW_H
#define LENTWINDOW_H

#include <QMainWindow>

namespace Ui {
class LentWindow;
}

class LentWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit LentWindow(QWidget *parent = nullptr);
    ~LentWindow();

private:
    Ui::LentWindow *ui;
};

#endif // LENTWINDOW_H
