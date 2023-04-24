from django.db import models


class People(models.Model) :
    # CharField等价于varchar
    # 属性名就是字段名，
    name = models.CharField(max_length = 50)
    # IntegerField等价于int
    age = models.IntegerField()
    # BooleanField等价于bool
    gender = models.BooleanField()


class Projects(models.Model) :
    # 在一个模型类中仅仅只能为一个字段指定primary_key=True
    # 一旦在模型类中的某个字段上指定了primary_key=True，那么ORM框架就不会自动创建名称为id的主键，否则会自动生成AutoField的id
    id = models.IntegerField(primary_key = True, verbose_name = '项目主键', help_text = '项目主键')

    # a.CharField类型必须指定max_length参数（改字段的最大字节数），其他是可选项：verbose_name和help_text是字段释义
    # b.如果需要给一个字段添加唯一约束，unique=True（默认为False）
    name = models.CharField(max_length = 20, verbose_name = '项目名称', help_text = '项目名称', unique = True)
    leader = models.CharField(max_length = 10, verbose_name = '项目负责人', help_text = '项目负责人')

    # c.使用default指定默认值（如果指定默认值后，在创建记录时，改字段传递，会使用默认值）
    is_execute = models.BooleanField(verbose_name = '是否启动项目', help_text = '是否启动项目', default = True)

    # d.null=True指定前端创建数据时，可以指定该字段为null，默认为null=False，DRF进行反序列化器输入时才有效
    #   null ：针对数据库，如果 null=True, 表示数据库的该字段可以为空，即在Null字段显示为YES。
    # e.blank=True指定前端创建数据时，可以指定该字段为空字符串，默认为blank=False，DRF进行反序列化器输入时才有效
    #   blank ：针对表单，如果 blank=True，表示你的表单填写该字段时可以不填，但是对数据库来说，没有任何影响
    desc = models.TextField(verbose_name = '项目描述信息', help_text = '项目描述信息',
                            null = True, blank = True, default = '')

    # f.在DateTimeField、DateField等字段中，指定auto_now_add=True，在创建一条记录时，会自动将创建记录时的时间作为该字段的值，后续在更新数据时，就不再修改
    # g.在DateTimeField、DateField等字段中，指定auto_now=True，在更新一条记录时，会自动将更新记录时的时间作为该字段的值
    create_time = models.DateTimeField(auto_now_add = True, verbose_name = '创建时间', help_text = '创建时间')
    update_time = models.DateTimeField(auto_now = True, verbose_name = '更新时间', help_text = '更新时间')

    # h.可以在任意一个模型类中创建Meta内部类，用于修改数据库的元数据信息
    class Meta :
        # i.db_table指定创建的数据表名称
        db_table = 'tb_projects'
        # 为当前数据表设置中文描述信息
        verbose_name = '项目表'
        verbose_name_plural = '项目表'
        ordering = ['id']

    def __str__(self) :
        return f"Projects({self.name})"

