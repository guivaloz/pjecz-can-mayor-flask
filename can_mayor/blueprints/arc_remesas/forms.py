"""
Archivo - Remesas, formularios
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Optional

from can_mayor.blueprints.arc_remesas_documentos.models import ArcRemesaDocumento
from can_mayor.blueprints.arc_remesas.models import ArcRemesa


class ArcRemesaNewForm(FlaskForm):
    """Formulario nueva Remesa"""

    num_oficio = StringField("Núm. Oficio: (núm/año)", validators=[DataRequired(), Length(max=16)])
    # anio = StringField("Años: (Años de inicio - Año final)", validators=[DataRequired()])
    tipo_documentos = SelectField("Tipo de Documentos", coerce=int, validate_choice=False, validators=[DataRequired()])
    crear = SubmitField("Crear")


class ArcRemesaEditForm(FlaskForm):
    """Formulario para editar Remesa"""

    # campos de solo lectura
    creado_readonly = StringField("Creado")
    juzgado_readonly = StringField("Instancia")
    tipo_documentos_readonly = StringField("Tipo de Documentos")
    # campos actualizables
    # anio = StringField("Años: (Años de inicio - Año final)", validators=[DataRequired()])
    num_oficio = StringField("Núm. Oficio: (núm/año)", validators=[DataRequired(), Length(max=16)])
    observaciones_solicitante = TextAreaField("Observaciones del Solicitante", validators=[Optional(), Length(max=256)])
    motivo = TextAreaField("Motivo", validators=[DataRequired(), Length(max=256)])
    guardar = SubmitField("Guardar")


class ArcRemesaAddDocumentForm(FlaskForm):
    """Formulario para añadir un documento a una Remesa"""

    remesas = SelectField("Remesa", coerce=int, validate_choice=False, validators=[DataRequired()])
    fojas = IntegerField("Fojas", validators=[DataRequired()])
    tipo_juzgado = SelectField("Tipo de Instancia", choices=ArcRemesaDocumento.TIPOS.items(), validators=[DataRequired()])
    observaciones = TextAreaField("Observaciones", validators=[Optional(), Length(max=256)])
    agregar = SubmitField("Agregar Documento")


class ArcRemesaAsignationForm(FlaskForm):
    """Formulario Asignación"""

    asignado = SelectField("Archivista", coerce=int, validate_choice=False, validators=[Optional()])
    asignar = SubmitField("Asignar")


class ArcRemesaRefuseForm(FlaskForm):
    """Formulario Rechazo"""

    anomalia_general = SelectField("Anomalía General", choices=ArcRemesa.ANOMALIAS.items(), validators=[DataRequired()])
    observaciones_archivista = TextAreaField("Observaciones por parte de Archivo", validators=[Optional(), Length(max=2048)])
    rechazar = SubmitField("Rechazar")


class ArcRemesaAnomaliaForm(FlaskForm):
    """Formulario Rechazo"""

    anomalia_general = SelectField("Anomalía General", choices=ArcRemesa.ANOMALIAS.items(), validators=[DataRequired()])
    observaciones_archivista = TextAreaField("Observaciones por parte de Archivo", validators=[Optional(), Length(max=2048)])
    guardar = SubmitField("Guardar")
    eliminar = SubmitField("Eliminar")
