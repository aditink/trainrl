#include <Python.h>
#include <caller.h>

int main() 
{
    PyImport_AppendInittab("caller", PyInit_caller);
    Py_Initialize();
    PyImport_ImportModule("caller");
    // Get an action using call_predict();
    action act = call_predict();
    // Print the action.
    printf("Action: %Lf %Lf %Lf %Lf\n", act.a1, act.a2, act.a3, act.a4);
    Py_Finalize();
    return 0;
}