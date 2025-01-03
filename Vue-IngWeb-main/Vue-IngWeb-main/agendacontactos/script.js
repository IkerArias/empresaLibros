new Vue({
  el: '#app',
  data: {
      contactos: [],
      nuevoContacto: {
          nombre: '',
          email: '',
          telefono: ''
      }
  },
  created() {
      // Cargar contactos desde LocalStorage al iniciar
      const contactosGuardados = localStorage.getItem('contactos');
      if (contactosGuardados) {
          this.contactos = JSON.parse(contactosGuardados);
      }
  },
  methods: {
      agregarContacto() {
          if (this.nuevoContacto.nombre && this.nuevoContacto.email && this.nuevoContacto.telefono) {
              this.contactos.push({ ...this.nuevoContacto });

              // Guardar contactos en LocalStorage
              localStorage.setItem('contactos', JSON.stringify(this.contactos));

              // Limpiar formulario
              this.nuevoContacto = { nombre: '', email: '', telefono: '' };
          } else {
              alert('Por favor, completa todos los campos');
          }
      },
      borrarContacto(index) {
          this.contactos.splice(index, 1);

          // Actualizar LocalStorage
          localStorage.setItem('contactos', JSON.stringify(this.contactos));
      }
  }
});
