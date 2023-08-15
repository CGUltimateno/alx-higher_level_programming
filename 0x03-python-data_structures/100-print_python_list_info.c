#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	long int s = PyList_Size(p);
	int x;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", obj->allocated);
	for ( = 0; x < s; x++)
		printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[i])->tp_name);
}