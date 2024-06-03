<template>
  <div class="attendance-control">
    <h2>Control de Asistencia con Reconocimiento Facial</h2>
    <video ref="video" width="640" height="480" autoplay></video>
    <button @click="captureImage">Capturar Imagen</button>
    <button @click="stopCamera">Detener Cámara</button>
    <div v-if="employeeName">
      Asistencia registrada para: {{ employeeName }}
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      employeeName: "",
      videoStream: null,
    };
  },
  mounted() {
    this.setupCamera();
  },
  methods: {
    async setupCamera() {
      const video = this.$refs.video;
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        this.videoStream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        video.srcObject = this.videoStream;
      }
    },
    captureImage() {
      const video = this.$refs.video;
      const canvas = document.createElement("canvas");
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      const context = canvas.getContext("2d");
      context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

      canvas.toBlob(async (blob) => {
        try {
          const formData = new FormData();
          formData.append("image", blob, "snapshot.jpg");
          const response = await fetch("http://127.0.0.1:5000/recognize", {
            method: "POST",
            body: formData,
          });
          console.log(response);
          const result = await response.json();
          this.employeeName = result.length > 0 ? result[0] : "Desconocido";
        } catch (e) {
          console.error(e);
        }
      }, "image/jpeg");
    },
    stopCamera() {
      if (this.videoStream) {
        this.videoStream.getTracks().forEach((track) => track.stop());
      }
    },
  },
};
</script>

<style>
.attendance-control {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}
h2 {
  text-align: center;
}
button {
  display: block;
  margin: 10px auto;
  padding: 10px 20px;
  font-size: 16px;
}
</style>
