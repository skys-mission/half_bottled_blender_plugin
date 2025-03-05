
Select the shape key of the mesh to be copied, go to the Scripting tab, and execute the following code to copy a shape key.

```python
import bpy
import numpy as np  

def duplicate_active_shape_key():
    obj = bpy.context.active_object 
    if not obj or obj.type  != 'MESH' or not obj.data.shape_keys: 
        raise Exception("Select a grid object with a shape key.")
        
    shape_keys = obj.data.shape_keys.key_blocks 
    active_index = obj.active_shape_key_index 

    if active_index < 0 or active_index >= len(shape_keys):
        raise Exception("Invalid shape key index.")
        
    src_key = shape_keys[active_index]

    new_key = obj.shape_key_add(name=f"{src_key.name}_copy",  from_mix=False)
    new_key.value  = src_key.value   

    mesh = obj.data 
    vert_count = len(mesh.vertices) 

    src_data = np.empty(vert_count  * 3, dtype=np.float32) 
    dst_data = np.empty_like(src_data) 
    
    src_key.data.foreach_get("co",  src_data)
    new_key.data.foreach_set("co",  src_data)

    obj.active_shape_key_index  = len(shape_keys) - 1

    bpy.context.view_layer.update() 

if __name__ == "__main__":
    try:
        duplicate_active_shape_key()
        print("Shape key copied successfully!")
    except Exception as e:
        print(f"err：{str(e)}")
```