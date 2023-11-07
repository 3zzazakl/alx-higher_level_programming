#include <Python.h>

/**
 * print_python_list_info - print info about lists.
 * @p: Pointer to python object.
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *ll;
	Py_ssize_t list_size, i;

	ll = (PyListObject *) p;
	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ll->allocated);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %ld: %s\n", i, ll->ob_item[i]->ob_type->tp_name);
	}
}
