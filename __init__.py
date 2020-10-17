import bpy
import math

# アドオン情報を記載
bl_info = {
    "name": "2oth F0x Builder",
    "author": "kamera25",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "F3 > 2oFox",
    "description": "Add like a 2oth F0x Model.",
    "warning": "",
    "doc_url": "https://kamera25.hatenadiary.jp/entry/f0xdoc",
    "category": "Add Mesh",
}



# 土台のモデル表示
def build_fox_base():
    
    # 土台部の頂点データ(汚いコードですみません...)
    _vertexsData = [
                 (-0.5,-0.5,0.4)
                ,(0.5,-0.5,0.4)
                ,(-0.5,0.5,0.4)
                ,(0.5,0.5,0.4)
                ,(-0.5,-0.5,0)
                ,(0.5,-0.5,0)
                ,(-0.5,0.5,0)
                ,(0.5,0.5,0)
                ,(-0.5,-0.5,0.9)
                ,(0.5,-0.5,0.9)
                ,(-0.5,0.5,0.9)
                ,(0.5,0.5,0.9)
                ,(-0.5,-0.5,0.8)
                ,(0.5,-0.5,0.8)
                ,(-0.5,0.5,0.8)
                ,(0.5,0.5,0.8)
                ,(-0.5,-0.5,1.4)
                ,(0.5,-0.5,1.4)
                ,(-0.5,0.5,1.4)
                ,(0.5,0.5,1.4)
                ,(-0.5,-0.5,1.3)
                ,(0.5,-0.5,1.3)
                ,(-0.5,0.5,1.3)
                ,(0.5,0.5,1.3)
                ,(-0.45,-0.45,1.3)
                ,(-0.45,0.45,1.3)
                ,(0.45,-0.45,1.3)
                ,(0.45,0.45,1.3)
                ,(-0.45,0.45,1.3)
                ,(0.45,0.45,1.3)
                ,(0.45,-0.45,1.3)
                ,(-0.45,-0.45,1.3)
                ,(-0.44,-0.44,0.4)
                ,(-0.44,0.44,0.4)
                ,(0.44,-0.44,0.4)
                ,(0.44,0.44,0.4)
                ,(-0.44,-0.44,0.45)
                ,(-0.44,0.44,0.45)
                ,(0.44,-0.44,0.45)
                ,(0.44,0.44,0.45)                     
    ]
    
    # 土台部の面データ(こっちも汚い...)
    _facesData = [
                 [1,3,35,34]
                ,[4,5,7,6]
                ,[0,4,5,1]
                ,[21,23,27,26]
                ,[2,6,4,0]
                ,[24,26,30,31]
                ,[8,9,11,10]
                ,[12,13,15,14]
                ,[16,17,19,18]
                ,[20,21,26,24]
                ,[19,17,21,23]
                ,[19,23,22,18]
                ,[18,22,20,16]
                ,[17,16,20,21]
                ,[9,8,12,13]
                ,[10,14,12,8]
                ,[11,15,14,10]
                ,[11,9,13,15]
                ,[22,20,24,25]
                ,[23,22,25,27]
                ,[31,30,29,28]
                ,[26,27,29,30]
                ,[25,24,31,28]
                ,[27,25,28,29]
                ,[3,7,6,2]
                ,[3,1,5,7]
                ,[35,33,37,39]
                ,[2,0,32,33]
                ,[3,2,33,35]
                ,[0,1,34,32]
                ,[36,38,39,37]
                ,[32,34,38,36]
                ,[34,35,39,38]
                ,[33,32,36,37]
    ]
                 
    _mesh = bpy.data.meshes.new( name='mesh')
    _mesh.from_pydata( _vertexsData, [], _facesData)
    _mesh.update()
    
    _obj = bpy.data.objects.new( 'fox', _mesh)
    _obj.data = _mesh
    
    _scene = bpy.context.scene
    _scene.collection.objects.link( _obj)


# ロゴフォントを表示させる
def build_logo_font( put_str, num_str):
    
    # テキストオブジェクトを追加
    bpy.ops.object.text_add()
    _selected = bpy.context.selected_objects[0]
    _selected.data.body = put_str
    
    # テキストオブジェクトの移動と回転
    bpy.ops.object.origin_set( type='GEOMETRY_ORIGIN')
    TOP_FONT_POS_Z = 2
    _putPos = TOP_FONT_POS_Z - num_str * 0.45
    _selected.location = ( 0, 0, _putPos)
    _deg = math.radians( 90 );
    _selected.rotation_euler = ( _deg, 0, 0)
    
    # テキストオブジェクトの縮小
    _size = 1.8 / len( put_str)
    _selected.scale = ( _size, 0.6, 1)
    
    # テキストオブジェクトの押し出し
    _selected.data.extrude = 0.4


# オペレータクラス
class OBJECT_OT_2othFox_object( bpy.types.Operator):
    """2oth Fox maker"""
    bl_idname = 'object.add_2ofox'
    bl_label = "2oth Foxぽいオブジェクトを作る"
    bl_options = { 'REGISTER', 'UNDO'}

    string_1st : bpy.props.StringProperty( name="一番上の文字")
    string_2nd : bpy.props.StringProperty( name="真ん中の文字")
    string_3rd : bpy.props.StringProperty( name="一番下の文字")


    def execute( self, context):

        if len( self.string_1st) != 0 :
            build_logo_font( self.string_1st, 1)
            
        if len( self.string_2nd) != 0 :
            build_logo_font( self.string_2nd, 2)
            
        if len( self.string_3rd) != 0 :
            build_logo_font( self.string_3rd, 3)
        
        build_fox_base()

        # 正常終了したことを返す
        return { 'FINISHED'}


# オペレーターとして登録する
def register():
    bpy.utils.register_class( OBJECT_OT_2othFox_object)

# 登録していたオペレーター解除する
def unregister():
    bpy.utils.unregister_class( OBJECT_OT_2othFox_object)

# 実行時に呼び出される(デバッグ用)
if __name__ == "__main__":
    register()