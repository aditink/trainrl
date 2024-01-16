#include <Python.h>
#include <caller.h>

int main() 
{
    PyImport_AppendInittab("caller", PyInit_caller);
    Py_Initialize();
    PyImport_ImportModule("caller");
    // Get an action using call_predict();
    state obs = {0.0, 0.1, 0.2, 0.3};
    action act = call_predict(obs);
    // Print the action.
    printf("Action: %Lf %Lf %Lf %Lf\n", act.a1, act.a2, act.a3, act.a4);
    Py_Finalize();
    return 0;
}