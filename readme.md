# how to use

'''bash
uvicorn main:app --reload'''

Пользователь крутит рулетку и ему выпадает одна из ячеек. После того, как ячейка выпала, она исключается из дальнейшего выпадения (т.е. в этом раунде рулетки она уже выпасть не может). Ячейка джекпот выпадает только после того как выпали все ячейки от 1 до 10. После того, как выпадает джекпот, раунд рулетки завершается и начинается новый раунд. Шанс выпадения каждой ячейки одинаковый.

Необходимо написать веб-приложение, которое крутит рулетку согласно указанной логике и согласно указанным весам. Для сохранения состояния раунда рулетки необходимо использовать БД. Также должен сохранятся в другой таблице лог выпадений ячеек.

Способ прокручивания рулетки - POST HTTP запрос с JSON данными. Дополнительно нужно реализовать функционал получения статистической информации (GET HTTP запрос с JSON ответом): Какое количество людей участвовало в рулетке (таблица, где в строке первый элемент это номер раунда рулетки, второй элемент количество пользователей) Список самых активных пользователей, где для каждого элемента нужно указать: айди пользователя количество раундов рулетке в которые он участвовал среднее количество прокручиваний рулетки за раунд

## примечания

Post-запрос принимается от чат бота.

Успешный результат сохраняется в базе данных

