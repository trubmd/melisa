# Melisa

## Описание
Melisa - это графическая оболочка для ядра системы компьютерной алгебры SageMath.
Вы работаете с Sage в интерактивной консоли (ноутбуке) jupyter qtconsole, которая
позволяет смешивать код, результаты вычислений и графики.
По сравнению с традиционной qtconsole, добавлена возможность сохранять и открывать
записные книжки с расширением .ipynb прямо в melisa.

## Что сделано
Реализовано простенькое меню со следующими функциями:
* Открыть в новом окне - открывает новое окно с новым автономным ядром
* Открыть - открывает файл с расширением .ipynb в текущем окне
* Открыть в новом окне - открывает файл с расширением .ipynb в новом окне
* Сохранить - сохраняет текущий ноутбук в формате .ipynb
* Выйти - выключает ядро и закрывает окно

## Зачем сделано
У SageMath нет своего графического интерфейса, подобно Mathematica или Maple. Чаще
всего с Sage работают в режиме терминала, Jupyter Notebook или Jupyter Lab.
Последние два обладают богатыми возможностями, но работают только через браузер.

С другой стороны, если вы хотите работать с Sage без браузера, отличным выбором был бы
jupyter qtconsole, но, к сожалению, там нет возможности сохранять и открывать ipynb-файлы.
Melisa - это попытка реализовать qtconsole + sagemath с возможностью сохранять и открывать
записные книжки, которой по умолчанию нет. 

## Дальнейшие планы
Расширение функционала приложения. Добавление в меню вкладок "Алгебра", "Анализ", "Графики" и т.д.
аналогично интерфейсу wxMaxima, чтобы пользователь мог выполнить какое-то стандартное действие (решить
уравнение, найти производную, взять интеграл, построить график функции и т.д.) без кода (особенно полезно новичкам)

## Операционная система
* Тестировал на Ubuntu 24.04

## Установка и запуск
Скопируйте и выполните:

```
git clone https://github.com/trubmd/melisa.git
cd melisa
chmod +x melisa_install.sh
./melisa_install.sh
```

Дождитесь установки. Потребуется некоторое время подождать, возможно,
вы даже успеете сварить и выпить чашечку кофе ;)

По окончанию установки запустите melisa

```
./melisa.sh
```
Теперь всегда вы сможете запускать melisa по этой команде.

## Обновление
Для обновления выполните:

```
rm -rf melisa
git clone https://github.com/trubmd/melisa.git
cd melisa
chmod +x melisa_update.sh
./melisa_update.sh
```
