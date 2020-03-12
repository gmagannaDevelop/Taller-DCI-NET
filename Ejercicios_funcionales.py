#!/usr/bin/env python
# coding: utf-8

# # Programación funcional en Python

# Veamos a nuestros nuevos amigos. He aquí una lista con una descripción increíblemente útil. Posteriormente los veremos en acción.
# 
# 1. ```lambda``` : Declarar una función anónima.
# 2. ```map``` : Mapear, se especifica primero la función y después el objeto.
# 3. ```filter``` : Filtrar para mantener elementos que cumplan con un criterio.
# 4. ```reduce``` : Aplicar una función cumulativa.
# 

# In[2]:


from functools import reduce


# La función reduce no es parte del espacio de nombres por defecto, por decisión del creador de Python : [Guido](https://github.com/gvanrossum). Por eso debemos importarla del módulo de herramientas para programación funcional functools.

# In[10]:


import numpy as np
import seaborn as sns
import pandas as pd


# ## Funciones anónimas

# **Utilidad** : Digamos que queremos calcular algo rápidamente, pero no queremos guardar una función que lo haga. Tal vez es una operación que se hará sólo una vez y no queremos "ocupar ese nombre", ahí usamos una función anónima o expresión lambda.
# 
# 1. **Sintaxis** : 

# $$ f(x) \; = \; x $$

# In[8]:


lambda x: x


# Ahora con varios argumentos : 
#     $$ f(x,y,x) \; = \; x\cdot y\cdot z $$

# In[9]:


lambda x, y, z: x*y*z


# 2. **Evaluación**
# 
# $$  f(x) = x^{x}\vert_{3} = 27 $$

# In[11]:


(lambda x: x**x)(3)


# Está muy bien eso de que sean anónimas pero, ¿y si yo quisiera guardar mi función?

# 3. **Asignación**

# In[13]:


cuadrado = lambda x: x**2


# In[14]:


cuadrado(3)


# 4. Funciones de orden superior

# In[16]:


aplica_función = lambda x, y: x(y)


# In[17]:


aplica_función(cuadrado, 3)


# 5. **Condicionales**
# 
# Digamos que quisiésemos saber si un valor es positivo.

# In[19]:


es_positivo = lambda x: True if x > 0 else False


# In[20]:


es_positivo(3)


# In[22]:


es_positivo(-np.pi)


# ## Mapear

# Hay diversas formas de llevar a cabo la misma operación. A continuación las abordaremos, pasando por clásicos hasta la forma funcional.
# 
# **Nuestra tarea :** Elevar una lista de números al cuadrado.
# ```python
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# ```

#     1. La forma tradicional, no pitónica :

# In[ ]:




