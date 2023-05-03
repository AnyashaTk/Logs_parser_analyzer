## Команда Maxpool

## ArenaData: создание утилиты интеграции журналов ADH для удобного визуального анализа

### Задание:

____

Необходимо создать решение, позволяющее для предоставленного кластера ADH агрегировать файлы логов (журналов) служб hadoop, обычно расположенных по пути /var/log/hadoop*. Также необходимо удобный инструмент просмотра/анализа агрегированных данных журнала. Форма анализа может быть произвольной — например в виде статистического отчета по различным видам событий/ошибок и т. д. Или интерактивный инструмент как показывающий статистику, так и позволяющий просматривать отдельные типы событий или даже информацию о событии. Для реализации приложения можно использовать любые библиотеки и/или вспомогательные инструменты, в т.ч. и высокоуровневые. 

### Ожидаемый результат:

____

По окончании работ необходимо продемонстрировать MVP программы,  при помощи которой получена требуемая в задании информация.  Также необходимо продемонстрировать полученный результат, а также объяснить его и подтвердить образцами данных из реальных журналов. 

### Практический результат:

____

1. Для проверки задания следует запустить файл server.py.

2. При выполнении задания были получены файлы логов (журналов) и создан инструмент просмотра/анализа агрегированных данных журнала.

3. В нашем случае пользователь имеет доступ к различно классифицированным ошибкам и предупреждениям, содержащихся в имеющихся логах.

4. Доступ к hadoob был получен с помощью ssh библиотеки paramiko и проложенного туннеля с помощью утилиты openvpn

5. Обновить данные логов можно при помощи отдельной кнопки на главной странице сайта.
