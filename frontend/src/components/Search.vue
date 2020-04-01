<template>
  <div>
    <v-container>
      <H1>SEARCH</H1>
      <div id="app-instasearch">
        <div class="input-container">
          <input
            type="text"
            placeholder="Type a name"
            v-model="authorNameSearchString"
          />
        </div>

        <ul>
          <li
            class="photo"
            v-for="photo in filteredPhotoFeed"
            v-bind:key="photo.id"
          >
            <img v-bind:src="photo.download_url" />
            <span class="author">{{ photo.author }}</span>
          </li>
        </ul>
        <!--
    v-for=”photo in filteredPhotoFeed”: Makes Vue able to repeat an li for each element in the filteredPhotoFeed array
    v-bind:key=”photo.id”: It’s important to choose a key to uniquely represent an image in order to be able to animate the list
    v-bind:src=”photo.download_url”: Without this, we won’t see the image
    {{ photo.author }}: To print the author name near each photo
    -->
      </div>

      {{ customers }}
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Customers",
  components: {},
  data() {
    return {
      months: [],
      month_detail: [],
      authorNameSearchString: "", // It will contain the search string bound to our input box
      photoFeed: null, // It will contain the array of images after download
      kundeNameSearchString: "",
      customers: null,
      axiosConfig: {
        headers: {
          Authorization: "Token " + this.$token.getToken()
        }
      }
    };
  },
  created() {
   
    this.allCustomers();
  },
  mounted() {
    axios
      .get("https://picsum.photos/v2/list?page=2&limit=10")
      .then(response => {
        this.photoFeed = response.data;
      })
      .catch(error => console.log(error));
  },
  methods: {
    allCustomers() {
      axios.get("api/customers/", this.axiosConfig).then(response => {
        this.customers = response.data;
      });
    }
  },
  computed: {
    filteredPhotoFeed: function() {
      var photos = this.photoFeed;
      var authorNameSearchString = this.authorNameSearchString;

      if (!authorNameSearchString) {
        return photos;
      }
    //var searchString;
      authorNameSearchString = authorNameSearchString.trim().toLowerCase();

      photos = photos.filter(function(item) {
        if (item.author.toLowerCase().indexOf(authorNameSearchString) !== -1) {
          return item;
        }
      });

      return photos;
    }
  }
};
</script>
<style>
.photo {
  list-style: none;
  display: grid;
  grid-template-columns: 200px auto;
  margin-top: 20px;
  align-items: center;
  background-color: #e9edf0;
  padding: 30px 50px;
  border-radius: 5px;
  border: 1px solid #e3e3e3;
}

.author {
  font-size: 25px;
  margin-left: 20px;
  color: #75818e;
}

.photo img {
  border-radius: 5px;
  width: 200px;
}
.input-container {
  border-radius: 5px;
  background: #677482;
  padding: 10px;
}

.input-container input {
  border: none;
  background: transparent;
  color: white;
  padding: 6px 15px;
  font-size: 18px;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #a6b0ba;
  opacity: 1; /* Firefox */
}
</style>
