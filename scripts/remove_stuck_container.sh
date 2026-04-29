#!/bin/bash

CONTAINER_NAME="vkclipbot"

echo "Попытка остановить контейнер '$CONTAINER_NAME'..."

if ! docker stop --time=10 "$CONTAINER_NAME" 2>/dev/null; then
    echo "docker stop не сработал, пробуем docker kill..."

    if ! docker kill "$CONTAINER_NAME" 2>/dev/null; then
        echo "docker kill не сработал, ищем PID процесса..."

        PID=$(docker inspect --format '{{.State.Pid}}' "$CONTAINER_NAME" 2>/dev/null)
        if [ -n "$PID" ] && [ "$PID" -gt 0 ]; then
            echo "Убиваем процесс с PID $PID..."
            kill -9 "$PID" && echo "Процесс $PID уничтожен."
        else
            echo "Не удалось получить PID контейнера."
        fi
    fi
fi

echo "Удаляем контейнер..."
docker rm -f "$CONTAINER_NAME" 2>/dev/null && echo "Контейнер удалён."

echo "Очистка зависших ресурсов Docker..."
docker system prune -f

echo ""
echo "Если контейнер всё ещё не удаляется, попробуйте:"
echo "  sudo systemctl restart docker"
echo "  или перезагрузите сервер"
