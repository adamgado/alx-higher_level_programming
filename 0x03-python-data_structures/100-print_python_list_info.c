#include "lists.h"
/**
 * print_python_list_info - Print some basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int a;
	long int size = Py_SIZE(p);
	PyListObject *obj = (PyListObject* )p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < size; a++)
	{
		printf("Element %d: %s\n", a, Py_TYPE(obj)->tp_name);

		obj = PyList_GetItem(p, a);
	}
}
