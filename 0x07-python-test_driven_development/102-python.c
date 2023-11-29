#include "Python.h"

/**
 * print_python_string - print info about string
 * @p: string obj.
 */

void print_python_string(PyObject *p)
{
long int length;

fflush(stdout);

print("[.] string object info\n");

if (strcmp(p->ob_type->tp_name, "str") != 0)
{
printf("  [ERROR] Invalid String Object");
return;
}

length = ((PyASCIIObject *)(p))->length;

if (PyUnicode_IS_COMPAT_ASCII(p))
printf("  type: compact ascii");
else
printf("  type: compact unicode object");

printf("  length: %ld\n", length);
printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
