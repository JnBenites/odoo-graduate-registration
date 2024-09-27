from odoo import models, fields

class Carrera(models.Model):
    _name = 'graduados_lista.carrera'  # Cambia "your_module" por el nombre real del módulo
    _description = 'Carrera'

    id_carrera = fields.Char(string='ID Carrera', required=True)
    codigo = fields.Char(string='Código', required=True)
    nombre_completo = fields.Char(string='Nombre Completo', required=True)


class Graduado(models.Model):
    _name = 'graduados_lista.graduado'  # Cambia "your_module" por el nombre real del módulo
    _description = 'Graduado'

    id_graduado = fields.Char(string='ID Graduado', required=True)
    nombre_completo = fields.Char(string='Nombre Completo', required=True)
    cedula = fields.Char(string='Cédula', required=True)
    correo_institucional = fields.Char(string='Correo Institucional', required=True)
    correo_personal = fields.Char(string='Correo Personal', required=True)
    provincia = fields.Char(string='Provincia', required=True)
    canton = fields.Char(string='Cantón', required=True)
    parroquia = fields.Char(string='Parroquia', required=True)
    ingreso = fields.Date(string='Fecha de Ingreso')
    culminacion = fields.Date(string='Fecha de Culminación')
    
    # Relación con Carrera
    titulo_obtenido_id = fields.Many2one('graduados_lista.carrera', string='Título Obtenido', ondelete='restrict')