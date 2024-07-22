#!/usr/bin/env bash

echo "[ 🤖 Iteration is started. ]"

# PROJECT ROOT FINDING START
PROJECT_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)
if [[ -f $PROJECT_ROOT/run_tests.sh && -f $PROJECT_ROOT/requirements.txt ]]; then
    echo "[ 🤖 Project root is \"$PROJECT_ROOT\". ]"
else 
    echo "[ 🛑 Project root \"$PROJECT_ROOT\" is incorrect! Iteration is stopped! ]"
    exit 1
fi
#PROJECT ROOT FINDING END

# SERVICE PARAMS START
CURRENT_TIME=$(date +%Y-%m-%d_%H-%M-%S)
TIME_FOR_MESSAGE=$(date +%H:%M:%S)
DATE_FOR_MESSAGE=$(date +%d.%m.%Y)
PYTEST_EXIT_CODE=1
# SERVICE PARAMS END

# Open project directory and activate virtual environment
echo "[ 🤖 Opening project root $PROJECT_ROOT... ]"
cd "$PROJECT_ROOT" || exit
echo "[ 🤖 Python virtual environment activating... ]"
source venv/bin/activate

# Preparation: Clearing results directory
echo "[ 🤖 Deleting old iterations from $PROJECT_ROOT/allure-results/... ]"
rm -rf "$PROJECT_ROOT"/allure-results/*

# Creating environments file
APP_VERSION="1.0.0"
touch "$PROJECT_ROOT"/allure-results/environment.properties
echo "Application\ version=$APP_VERSION" >> "$PROJECT_ROOT"/allure-results/environment.properties


RUN_SCOPE_WITH_PYTEST_ARGS="tests"
# Parsing RUN_SCOPE variable
if [ -z "${RUN_SCOPE}" ]; then
    echo "[ 🤖 RUN_SCOPE is not defined. Using default scope: \"$RUN_SCOPE_WITH_PYTEST_ARGS\" without additional args...  ]"
else
    RUN_SCOPE_WITH_PYTEST_ARGS="$RUN_SCOPE"
    echo "[ 🤖 Defined RUN_SCOPE and additional args is: \"$RUN_SCOPE_WITH_PYTEST_ARGS\"... ]"
fi

pytest "$RUN_SCOPE_WITH_PYTEST_ARGS" \
--alluredir="$PROJECT_ROOT"/allure-results \
-s

PYTEST_EXIT_CODE=$?
echo "[ 🤖 Pytest exitcode is $PYTEST_EXIT_CODE. ]"

echo "[ 🤖 Generating single-file report with Allure... ]"
allure generate "$PROJECT_ROOT"/allure-results --clean --output "$PROJECT_ROOT"/allure-report/"$CURRENT_TIME"/ --single-file --name "Py Money Calculator Tests"


[ $PYTEST_EXIT_CODE -eq 0 ] && RUN_STATUS_FOR_BASH='🟩 Статус: все тесты пройдены.' || RUN_STATUS_FOR_BASH="🟥 Статус: обнаружены упавшие тесты."
echo "[ 🤖 Отчёт об итерации: ]"
echo "   ---- "
echo "   ⚙️ Итерация тестирования от $TIME_FOR_MESSAGE ($DATE_FOR_MESSAGE) завершена."
echo "   $RUN_STATUS_FOR_BASH"
echo "   🔗 Локальная ссылка на отчёт: ./allure-report/$CURRENT_TIME/index.html"
echo "   ---- "

# Deactivate virtual environment
echo "[ 🤖 Python virtual environment deactivating... ]"
deactivate

# Open report with open
SYSTEM_HAS_OPEN=$(which open | grep 'open')
if [ -n "$SYSTEM_HAS_OPEN" ]
then
    echo "[ 🤖 Report opening... ]"
    open ./allure-report/"$CURRENT_TIME"/index.html > /dev/null
else
   echo "[ 🤖 open not found, the report will not be opened. ]"
fi

echo "[ 🤖 Iteration is ended. ]"